# Distribution of Key Outcomes
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
sns.histplot(df['Yield_Tonnes_Ha'], kde=True, ax=axes[0]).set_title('Distribution of Yield')
sns.histplot(df['Profit_INR'], kde=True, ax=axes[1]).set_title('Distribution of Profit')
plt.show()

# Categorical Frequencies
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
sns.countplot(data=df, x='Season', ax=axes[0]).set_title('Records per Season')
sns.countplot(data=df, x='Irrigation_Method', ax=axes[1]).set_title('Records per Irrigation Method')
plt.show()
