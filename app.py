# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:25:46 2026

@author: Admin
"""

import streamlit as st
from core.generator import generate_system
from core.plotter import plot_system
from utils.checker import check_point
from ai.tutor_ai import ask_ai



#st.set_page_config(layout="wide")
st.title("🤖 Hệ thống hỗ trợ bài tập phần Đại số lớp 10")
# ======================
# Tabs chính
# ======================
tab1, tab2, tab3, tab4 = st.tabs(["📘 Tạo Bài tập", "📊 Đồ thị", "🤖 AI", "🎯 Luyện tập"])

# ======================
# TAB 1: TẠo Đề bài BÀI TẬP
# ======================

with tab1:
   
     st.subheader("Nhập hệ bất phương trình")
    
    
     # ===== Hàm tạo 1 dòng phương trình =====
     def input_row(key_prefix):
         cols = st.columns([1,2,1,2,1,2,1,2])
     
         with cols[0]:
             st.markdown("**a:**")
         with cols[1]:
             a = st.number_input("", key=f"{key_prefix}_a", label_visibility="collapsed")
     
         with cols[2]:
             st.markdown("**b:**")
         with cols[3]:
             b = st.number_input("", key=f"{key_prefix}_b", label_visibility="collapsed")
     
         with cols[4]:
             st.markdown("**c:**")
         with cols[5]:
             c = st.number_input("", key=f"{key_prefix}_c", label_visibility="collapsed")
     
         with cols[6]:
             st.markdown("**sign:**")
         with cols[7]:
             sign = st.selectbox("", [">=", "<="], key=f"{key_prefix}_sign", label_visibility="collapsed")
     
         return a, b, c, sign
    
    
     st.markdown("""
    <style>
    div[data-testid="stNumberInput"] input {
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True) 
    
    # ===== Phương trình 1 =====
     st.markdown("**Bất phương trình 1**")
     a1, b1, c1, sign1 = input_row("pt1")
     
     # ===== Phương trình 2 =====
     st.markdown("**Bất phương trình 2**")
     a2, b2, c2, sign2 = input_row("pt2")
     
     
     # ===== Nút nhập =====
     if st.button("📥 Nhập hệ"):
         st.session_state.system = [
             (a1, b1, c1, sign1),
             (a2, b2, c2, sign2)
         ]
         
     if st.button("📥 Sinh hệ ngẫu nhiên"):
         st.session_state.system = generate_system()
         #st.write(st.session_state.system)
         
     def format_expr(a,b,c,s):
         return f"{a}x {'+' if b>=0 else '-'} {abs(b)}y {'+' if c>=0 else '-'} {abs(c)} {s} 0"
     
     if "system" in st.session_state:
         st.markdown("### 📘 Hệ đã nhập:")
     
         for (a,b,c,s) in st.session_state.system:
             st.latex(format_expr(a,b,c,s))
     
 
 


# ======================
# TAB 2: ĐỒ THỊ
# ======================
with tab2:
    if "system" in st.session_state:
    
        st.subheader("Chọn phương trình hiển thị")
    
        active_system = []
        for i, (a,b,c,s) in enumerate(st.session_state.system):
            if st.checkbox(f"PT {i+1}: {a}x + {b}y + {c} {s} 0", value=True,key=f"mpl_checkbox_{i}"):
                active_system.append((a,b,c,s))
    
        fig = plot_system(active_system)
        st.pyplot(fig)
    
       
    st.subheader("📍 Kiểm tra điểm thuộc miền nghiêm?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        x0 = st.number_input("x0", value=0.0)
    
    with col2:
        y0 = st.number_input("y0", value=0.0)
    
    if st.button("Kiểm tra"):
        ok = True
    
        for (a,b,c,s) in st.session_state.system:
            val = a*x0 + b*y0 + c
    
            if s == ">=" and val < 0:
                ok = False
            if s == "<=" and val > 0:
                ok = False
    
        if ok:
            st.success("✅ Điểm thuộc miền nghiệm")
        else:
            st.error("❌ Điểm không thuộc miền")
       
       
    st.subheader("🎯 Chọn vùng (bằng điểm đại diện)")
    
    x_test = st.number_input("Chọn x", key="test_x")
    y_test = st.number_input("Chọn y", key="test_y")
    
    if st.button("Xác nhận vùng"):
        ok = True
    
        for (a,b,c,s) in st.session_state.system:
            val = a*x_test + b*y_test + c
    
            if s == ">=" and val < 0:
                ok = False
            if s == "<=" and val > 0:
                ok = False
    
        if ok:
            st.success("🎉 Bạn đã chọn đúng miền nghiệm!")
        else:
            st.warning("⚠️ Vùng này không thỏa hệ")       
        
    

# ======================
# TAB 3: AI
# ======================
with tab3:
    sub1, sub2, sub3, sub4 = st.tabs(["Gợi ý", "Ngắn gọn", "Chi tiết", "Sai lầm"])

    if "system" in st.session_state:
        with sub1:
            st.write(ask_ai(st.session_state.system, "hint"))

        with sub2:
            st.write(ask_ai(st.session_state.system, "short"))

        with sub3:
            st.write(ask_ai(st.session_state.system, "detail"))

        with sub4:
            st.write(ask_ai(st.session_state.system, "mistake"))

# ======================
# TAB 4: LUYỆN TẬP
# ======================
with tab4:
    sub1, sub2 = st.tabs(["Chọn điểm", "5 bài"])

    with sub1:
        if "system" in st.session_state:
            x = st.number_input("x luyện")
            y = st.number_input("y luyện")

            if st.button("Check"):
                if check_point(st.session_state.system, x, y):
                    st.success("Đúng")
                else:
                    st.error("Sai")

    with sub2:
        if st.button("Sinh 5 bài"):
            for _ in range(5):
                st.write(generate_system())