# Relationship between Rainfall and Yield by Season
sns.lmplot(data=df, x='Rainfall_mm', y='Yield_Tonnes_Ha', hue='Season', aspect=1.5)
plt.title('Rainfall vs Yield by Season')
plt.show()

# Feature Importance via simple Linear Regression
from sklearn.linear_model import LinearRegression

# Prepare features (using the derived/cleaned numeric columns)
features = ['Rainfall_mm', 'Avg_Temperature', 'Fertilizer_kg_ha', 'Soil_Moisture_pct']
regression_data = df.dropna(subset=features + ['Yield_Tonnes_Ha'])

X = regression_data[features]
y = regression_data['Yield_Tonnes_Ha']

if not X.empty:
    model = LinearRegression().fit(X, y)
    importance = pd.Series(model.coef_, index=features)
    print("Simple Regression Coefficients (Impact on Yield):")
    print(importance.sort_values(ascending=False))
else:
    print("Insufficient data for regression analysis.")
