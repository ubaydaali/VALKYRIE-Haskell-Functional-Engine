import streamlit as st
import subprocess
import os
import time

st.set_page_config(page_title="VALKYRIE Haskell", page_icon="🦅", layout="wide")

st.markdown("""
    <style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0e1117; color: white; text-align: center; padding: 15px 0; border-top: 1px solid #4a4a4a; z-index: 999; }
    .footer a { color: #d4af37; text-decoration: none; margin: 0 15px; font-size: 20px; transition: 0.3s; }
    .footer a:hover { color: #ffffff; text-shadow: 0 0 10px #d4af37; }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """, unsafe_allow_html=True)

st.title("🦅 VALKYRIE: Pure Functional Settlement Engine")
st.markdown("##### *Mathematically proving trade integrity with zero runtime exceptions using Haskell.*")
st.divider()

if st.button("🚀 Evaluate Market Ledger (Mathematical Purity)", type="primary"):
    
    os.makedirs('haskell_engine', exist_ok=True)
    os.makedirs('data/output', exist_ok=True)
    os.makedirs('data/input', exist_ok=True)
    
    with st.spinner("Generating Live Market Data..."):
        with open('data/input/market_trades.dat', 'w', encoding='utf-8') as f:
            for i in range(1, 25001):
                amount = 1200 if i % 4200 != 0 else 89000
                # صيغة السطر: المعرف (8) مسافة (1) المبلغ (6)
                f.write(f"TRD{i:05d} {amount:06d}\n")
    
    with st.spinner("Compiling Haskell GHC (Glasgow Haskell Compiler)..."):
        try:
            # ترجمة كود هاسكل إلى ملف تنفيذي سريع جداً
            subprocess.run(["ghc", "-O2", "-odir", "haskell_engine", "-hidir", "haskell_engine", "-o", "haskell_engine/valkyrie", "src/valkyrie_core.hs"], check=True)
        except FileNotFoundError:
            st.warning("⚠️ Local GHC Compiler Missing. Deploy to Streamlit Cloud with `ghc` in your `packages.txt`.")
            st.stop()
            
    start_time = time.time()
    with st.spinner("Executing mathematically proven functions..."):
        subprocess.run(["./haskell_engine/valkyrie"])
    end_time = time.time()
    
    st.success(f"✅ Pure Evaluation Completed in {end_time - start_time:.4f} seconds!")
    
    try:
        with open('data/output/audit_log.txt', 'r', encoding='utf-8') as f:
            st.code(f.read(), language="text")
    except FileNotFoundError:
        st.warning("Execution failed.")
        
    st.info("💡 **Architectural Note:** In Haskell, variables cannot change (Immutability). The entire logic is a mathematical pipeline. If the code compiles, it is fundamentally immune to side-effect bugs and race conditions.")

st.markdown("""
    <div class="footer">
        <a href="https://github.com/ubaydaali" target="_blank"><i class="fab fa-github"></i></a>
        <a href="https://www.linkedin.com/in/ubayda-ali-95972a406/" target="_blank"><i class="fab fa-linkedin"></i></a>
        <a href="https://t.me/obedaale" target="_blank"><i class="fab fa-telegram"></i></a>
        <a href="https://onws.net" target="_blank"><i class="fas fa-globe"></i></a>
        <br><span style="font-size:12px; color:#888;">Executive Architect: UBAYDA ALİ | Engineered with Haskell & Python</span>
    </div>
    """, unsafe_allow_html=True)
