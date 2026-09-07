import datetime
import pandas as pd
import plotly.express as px
import streamlit as st
from expense_ops import init_db, add_expense_db, get_expenses_db, delete_expenses_batch

# 1. 페이지 세팅
st.set_page_config(
    page_title="스마트 지출 관리",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)
init_db()

# 2. 커스텀 CSS (불필요한 공백 제거 및 카드 스타일)
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', -apple-system, sans-serif !important; }

    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 1280px;
    }

    /* KPI 카드 디자인 */
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 18px 22px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }
    .metric-label { font-size: 0.85rem; font-weight: 600; color: #64748B; margin-bottom: 4px; }
    .metric-val { font-size: 1.7rem; font-weight: 800; color: #0F172A; }
    .metric-sub { font-size: 0.8rem; color: #94A3B8; margin-top: 4px; }

    /* 플랫 입력 컨테이너 */
    .action-panel {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 16px 20px;
        margin-top: 1rem;
        margin-bottom: 1.8rem;
    }

    button[kind="primary"] {
        border-radius: 8px !important;
        font-weight: 700 !important;
    }
    button[kind="secondary"] {
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 헤더 영역 (정상적인 제목, 설명 문구 및 빈 바 완전 제거)
h_left, h_right = st.columns([5, 1])
with h_left:
    st.markdown("<h2 style='margin:0; font-weight:800; color:#0F172A;'>💰 스마트 지출 관리</h2>", unsafe_allow_html=True)
with h_right:
    if st.button("🔄 새로고침", use_container_width=True):
        st.rerun()

# 4. 상단 퀵 입력 바
CATEGORY_LIST = ["🍚 식비", "☕ 카페/간식", "🚌 교통", "🛍️ 쇼핑", "🏠 주거/통신", "🎉 문화/여가", "💊 의료/건강", "기타"]

st.markdown("<div class='action-panel'>", unsafe_allow_html=True)
with st.form("quick_add_form", clear_on_submit=True):
    col_date, col_cat, col_desc, col_amt, col_btn = st.columns([1.5, 1.8, 3.5, 2.2, 1.4])
    
    with col_date:
        inp_date = st.date_input("결제일자", datetime.date.today())
    with col_cat:
        inp_cat = st.selectbox("카테고리", CATEGORY_LIST)
    with col_desc:
        inp_desc = st.text_input("지출 내용", placeholder="예: 점심 식사")
    with col_amt:
        inp_amt = st.number_input("지출 금액 (원)", min_value=0, step=1000, value=0)
    with col_btn:
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        submitted = st.form_submit_button("기록 추가", type="primary", use_container_width=True)

    if submitted:
        if not inp_desc.strip():
            st.toast("⚠️ 지출 내용을 입력해 주세요.")
        elif inp_amt <= 0:
            st.toast("⚠️ 금액은 0원보다 커야 합니다.")
        else:
            add_expense_db(str(inp_date), inp_cat, inp_desc.strip(), inp_amt)
            st.toast("✅ 정상 등록되었습니다.")
            st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# 5. 데이터 로드
expenses = get_expenses_db()

if not expenses:
    st.info("등록된 지출 내역이 없습니다. 위 입력창에서 첫 지출을 기록해 보세요.")
    st.stop()

df = pd.DataFrame(expenses)

# 6. 상단 요약 카드 (KPIs)
total_sum = df["amount"].sum()
tx_count = len(df)
avg_ticket = int(total_sum / tx_count)
max_row = df.loc[df["amount"].idxmax()]

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-label'>총 지출 누적</div>
        <div class='metric-val' style='color:#2563EB;'>{total_sum:,} <span style='font-size:1rem; font-weight:600;'>원</span></div>
        <div class='metric-sub'>전체 기간 누적 정산</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-label'>총 결제 횟수</div>
        <div class='metric-val'>{tx_count:,} <span style='font-size:1rem; font-weight:600;'>건</span></div>
        <div class='metric-sub'>정상 트랜잭션 기록</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-label'>건당 평균 단가</div>
        <div class='metric-val'>{avg_ticket:,} <span style='font-size:1rem; font-weight:600;'>원</span></div>
        <div class='metric-sub'>평균 소비 단가</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-label'>단일 최대 지출</div>
        <div class='metric-val' style='color:#DC2626;'>{max_row['amount']:,} <span style='font-size:1rem; font-weight:600;'>원</span></div>
        <div class='metric-sub'>{max_row['description']}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# 7. 메인 뷰 (좌우 2분할)
main_left, main_right = st.columns([1.35, 1.0], gap="large")

# [좌측] 지출 목록 및 선택 삭제
with main_left:
    st.markdown("<h4 style='margin:0 0 10px 0; font-weight:700;'>지출 내역 및 관리</h4>", unsafe_allow_html=True)

    all_cats = ["전체"] + sorted(list(df["category"].unique()))
    selected_filter = st.segmented_control(
        "카테고리 필터",
        options=all_cats,
        default="전체",
        label_visibility="collapsed"
    )

    filtered_df = df if selected_filter == "전체" else df[df["category"] == selected_filter]

    grid_source = filtered_df.copy()
    grid_source["선택"] = False

    grid_display = grid_source[["선택", "id", "date", "category", "description", "amount"]]

    edited_table = st.data_editor(
        grid_display,
        column_config={
            "선택": st.column_config.CheckboxColumn("선택", help="삭제할 항목을 선택하세요", default=False),
            "id": st.column_config.NumberColumn("ID", disabled=True),
            "date": st.column_config.TextColumn("날짜", disabled=True),
            "category": st.column_config.TextColumn("분류", disabled=True),
            "description": st.column_config.TextColumn("내용", disabled=True),
            "amount": st.column_config.NumberColumn("금액", format="%d원", disabled=True),
        },
        disabled=["id", "date", "category", "description", "amount"],
        hide_index=True,
        use_container_width=True,
        height=380
    )

    act_col1, act_col2 = st.columns([1, 1])
    with act_col1:
        selected_ids = edited_table[edited_table["선택"]]["id"].tolist()
        btn_label = f"🗑️ 선택 {len(selected_ids)}건 삭제" if selected_ids else "🗑️ 선택 삭제"
        if st.button(btn_label, type="secondary", disabled=not bool(selected_ids), use_container_width=True):
            delete_expenses_batch(selected_ids)
            st.toast("삭제가 완료되었습니다.")
            st.rerun()

    with act_col2:
        csv_file = filtered_df[["date", "category", "description", "amount"]].to_csv(index=False, encoding="utf-8-sig")
        st.download_button("📥 내역 CSV 다운로드", data=csv_file, file_name="expenses.csv", mime="text/csv", use_container_width=True)

# [우측] 시각화 차트
with main_right:
    st.markdown("<h4 style='margin:0 0 10px 0; font-weight:700;'>소비 패턴 분석</h4>", unsafe_allow_html=True)

    tab_pie, tab_trend = st.tabs(["카테고리별 비중", "일자별 지출 추세"])

    with tab_pie:
        cat_agg = df.groupby("category")["amount"].sum().reset_index()
        top_category = cat_agg.sort_values(by="amount", ascending=False).iloc[0]
        ratio = int((top_category["amount"] / total_sum) * 100)

        st.markdown(f"""
        <div style='background:#F1F5F9; border-left:4px solid #2563EB; border-radius:8px; padding:10px 14px; margin: 6px 0 14px 0;'>
            <span style='font-size:0.88rem; color:#334155;'>
                현재 <b>{top_category['category']}</b> 항목에 전체의 <b>{ratio}%</b>({top_category['amount']:,}원)를 사용했습니다.
            </span>
        </div>
        """, unsafe_allow_html=True)

        fig_pie = px.pie(
            cat_agg,
            values="amount",
            names="category",
            hole=0.6,
            color_discrete_sequence=["#2563EB", "#38BDF8", "#818CF8", "#F472B6", "#FB923C", "#FBBF24", "#A3E635", "#94A3B8"]
        )
        fig_pie.update_traces(textposition="outside", textinfo="percent+label", showlegend=False)
        fig_pie.update_layout(margin=dict(t=20, b=20, l=20, r=20), height=310)
        
        # 첫 번째 사진 해결: 상단 툴바(카메라, 줌 등) 숨김
        st.plotly_chart(fig_pie, use_container_width=True, config={'displayModeBar': False})

    with tab_trend:
        daily_df = df.groupby("date")["amount"].sum().reset_index().sort_values("date")
        # 날짜 문자열 보장
        daily_df["date"] = daily_df["date"].astype(str)

        fig_trend = px.bar(
            daily_df,
            x="date",
            y="amount",
            color_discrete_sequence=["#2563EB"]
        )
        # 두 번째 사진 해결: 날짜 축을 category(문자열 범주)로 고정하여 밀리초 쪼개짐 방지
        fig_trend.update_layout(
            xaxis_title="",
            yaxis_title="지출액 (원)",
            xaxis=dict(type='category'),
            margin=dict(t=20, b=20, l=10, r=10),
            height=340
        )
        
        # 첫 번째 사진 해결: 상단 툴바 숨김
        st.plotly_chart(fig_trend, use_container_width=True, config={'displayModeBar': False})