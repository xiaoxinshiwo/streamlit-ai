import numpy as np
import pandas as pd

# 设置年份和省市
years = list(range(2014, 2025))
provinces = ['北京', '上海', '广东', '浙江', '江苏', '山东', '四川', '湖北', '湖南', '福建', '河南', '河北', '辽宁',
			 '陕西', '重庆', '天津']

# 初始化空列表存储数据
data = []

# 随机生成数据
for year in years:
	for province in provinces:
		# 假设每年每省出生人口在20万到100万之间
		total_births = np.random.randint(200000, 1000000)
		male_births = np.random.randint(total_births // 2, total_births)  # 男性出生人数
		female_births = total_births - male_births  # 女性出生人数

		# 假设考上大学人数为出生人口的5%到20%之间
		college_students = np.random.randint(int(0.05 * total_births), int(0.2 * total_births))

		# 假设就业人数为考上大学人数的50%到90%
		employed = np.random.randint(int(0.5 * college_students), int(0.9 * college_students))

		# 添加数据到列表
		data.append([year, province, total_births, male_births, female_births, college_students, employed])

# 创建DataFrame
df = pd.DataFrame(data, columns=['Year', 'Province', 'Total Births', 'Male Births', 'Female Births', 'College Students',
								 'Employed'])

# 保存至CSV文件
csv_file_path = '../data/china_population_births_2014_2024.csv'
df.to_csv(csv_file_path, index=False, encoding='utf-8')
