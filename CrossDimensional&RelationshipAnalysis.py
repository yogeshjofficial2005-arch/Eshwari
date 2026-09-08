# Season x Crop Heatmap
# Identify if specific crop-season combinations outperform others
pivot_yield = df.pivot_table(values='Yield_Tonnes_Ha', index='Crop', columns='Season', aggfunc='mean')
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_yield, annot=True, cmap='YlGnBu')
plt.title('Average Yield by Crop and Season')
plt.show()

# Correlation Analysis (Numerical columns only)
plt.figure(figsize=(12, 10))
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()
sns.heatmap(corr, annot=False, cmap='coolwarm', center=0)
plt.title('Overall Correlation Heatmap')
plt.show()
