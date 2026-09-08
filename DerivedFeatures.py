# Ensure the dataframe exists from the previous cell
if 'df' not in locals() or df.empty:
    print("Error: Dataframe 'df' is not defined. Please run the data extraction cell (6be2598b) first.")
else:
    # Check for duplicates
    duplicates = df.duplicated(subset=['Farm_ID']).sum()
    print(f"Duplicate Farm_IDs: {duplicates}")

    # Handle missing values
    missing_pct = df.isnull().mean() * 100
    print("\nPercentage of missing values per column:")
    print(missing_pct[missing_pct > 0])

    # Fill missing numeric values with median (robust to outliers)
    numeric_cols_to_fix = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols_to_fix] = df[numeric_cols_to_fix].fillna(df[numeric_cols_to_fix].median())

    # Logical Validation
    # Revenue ≈ Production * Market_Price
    # Profit = Revenue - Total_Cost
    df['Calculated_Revenue'] = df['Production_Tonnes'] * df['Market_Price_INR']
    df['Revenue_Diff'] = (df['Revenue_INR'] - df['Calculated_Revenue']).abs()

    # Derived Features
    df['Profit_Margin_pct'] = (df['Profit_INR'] / df['Revenue_INR']) * 100
    df['Cost_per_Hectare'] = df['Total_Cost_INR'] / df['Farm_Area_Hectares']
    df['Yield_per_mm_Rainfall'] = df['Yield_Tonnes_Ha'] / df['Rainfall_mm'].replace(0, np.nan)

    # Binning Environmental Factors
    df['Rainfall_Category'] = pd.qcut(df['Rainfall_mm'], 3, labels=["Low", "Medium", "High"])
    df['Temp_Category'] = pd.qcut(df['Avg_Temperature'], 3, labels=["Low", "Medium", "High"])

    print("\nDerived features created successfully.")
    display(df[['Profit_Margin_pct', 'Cost_per_Hectare', 'Yield_per_mm_Rainfall']].head())
