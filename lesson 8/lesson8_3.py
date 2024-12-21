import pandas as pd
from tools import fetch_youbike_data
import streamlit as st

youbike_data:list[dict]=fetch_youbike_data()

#使用streamlit分2個欄位
#使用youBike_data:list的資料，取出所有的行政區域(sarea),不可重複
# 左邊是行政區域(sarea)，使用下拉式表單
# 右邊是該行政區域的YouBike站點資訊的表格資料
#最下方顯示該行政區域的YouBike站點資訊的地圖
# 使用streamlit分2個欄位
col1, col2 = st.columns([1,3])

# 使用youBike_data:list的資料，取出所有的行政區域(sarea),不可重複
sareas = list(set([item['sarea'] for item in youbike_data]))

# 左邊是行政區域(sarea)，使用下拉式表單
with col1:
    selected_sarea = col1.selectbox('選擇行政區域', sareas)

# 右邊是該行政區域的YouBike站點資訊的表格資料
filtered_data = [item for item in youbike_data if item['sarea'] == selected_sarea]
with col2:
    st.write('該行政區域的YouBike站點資訊')
    show_data =[{'站點':item['sna'],
                 '總車輛數':item['tot'],
                 '可藉車輛數':item['sbi'],
                 '可還空位數':item['bemp'],
                 'lat':item['lat'],
                 'lng':item['lng']} for item in filtered_data]
    st.dataframe(show_data, height=300, use_container_width=True)
   
# 最下方顯示該行政區域的YouBike站點資訊的地圖

df = pd.DataFrame(filtered_data)
df['lat'] = pd.to_numeric(df['lat'])
df['lng'] = pd.to_numeric(df['lng'])
st.map(df.rename(columns={'lat': 'latitude', 'lng': 'longitude'}))

