# High Input, Low Yield Anomaly (Inefficiency Analysis)
threshold_yield = df['Yield_Tonnes_Ha'].quantile(0.25)
threshold_cost = df['Total_Cost_INR'].quantile(0.75)

inefficient_farms = df[(df['Yield_Tonnes_Ha'] < threshold_yield) & (df['Total_Cost_INR'] > threshold_cost)]
print(f"Found {len(inefficient_farms)} farms classified as 'High Cost, Low Yield'.")
display(inefficient_farms[['Farm_ID', 'Crop', 'Season', 'Yield_Tonnes_Ha', 'Total_Cost_INR', 'Profit_INR']].head())
