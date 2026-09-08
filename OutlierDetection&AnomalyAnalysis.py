# Statistical Outlier Detection using Z-score
from scipy import stats

# Focus on Yield and Profit outliers
target_cols = ['Yield_Tonnes_Ha', 'Profit_INR']
z_scores = np.abs(stats.zscore(df[target_cols].fillna(df[target_cols].median())))
outliers = df[(z_scores > 3).any(axis=1)]

print(f"Number of statistical outliers identified (Z > 3): {len(outliers)}")
display(outliers[['Farm_ID', 'Season', 'Crop', 'Yield_Tonnes_Ha', 'Profit_INR']].head())

# Visualizing the Yield vs Profit landscape
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Yield_Tonnes_Ha', y='Profit_INR', hue='Season', alpha=0.6)
plt.title('Profit vs Yield Distribution across Seasons')
plt.show()
