# Seasonal Yield Comparison
# Ensure we drop NaNs for the ANOVA and plot
df_clean = df.dropna(subset=['Season', 'Yield_Tonnes_Ha'])

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_clean, x='Season', y='Yield_Tonnes_Ha')
plt.title('Yield Comparison Across Seasons')
plt.show()

# One-way ANOVA
groups = [df_clean[df_clean['Season'] == s]['Yield_Tonnes_Ha'] for s in df_clean['Season'].unique()]
f_stat, p_val = stats.f_oneway(*groups)
print(f"ANOVA Result for Yield: F={f_stat:.4f}, p={p_val:.4f}")

if p_val < 0.05:
    print("Statistically significant difference detected. Performing Tukey HSD...")
    tukey = pairwise_tukeyhsd(endog=df_clean['Yield_Tonnes_Ha'], groups=df_clean['Season'], alpha=0.05)
    print(tukey)
