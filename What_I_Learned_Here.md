## 1️⃣ Matplotlib vs Seaborn

* **Matplotlib (`plt`)**: Low-level plotting, more control over individual elements.
* **Seaborn (`sns`)**: High-level statistical plots, easier for complex visualizations like histograms with KDE, countplots, boxplots, violin plots, etc.
* **Rule of thumb**:

  * Use **Seaborn** for quick statistical plots with nice styling.
  * Use **Matplotlib** for custom plots or when Seaborn doesn’t have a built-in plot (e.g., pie charts).

---

## 2️⃣ Figure and Subplots

* Create multiple subplots:

```python
fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))
```

* **Access each subplot**:

```python
sns.histplot(..., ax=ax[0])  # 1D
sns.barplot(..., ax=ax[1,0]) # 2D
```

* `plt.tight_layout()` avoids overlapping labels.

---

## 3️⃣ Pie Charts with Matplotlib

* Single-line, object-oriented style:

```python
ax.pie(values, labels=labels, explode=[0.1,0,0], autopct='%1.1f%%', colors=plt.cm.tab20.colors)
ax.axis('off')  # hide axis for pie charts
```

* Avoid manually specifying many colors; use `plt.cm` colormaps for automatic scaling.

---

## 4️⃣ Countplots & Bar Labels

* Countplot with labels:

```python
sns.countplot(x='gender', data=df, palette='bright', ax=ax[0])
[ax[0].bar_label(c, color='black', size=15) for c in ax[0].containers]
```

* `bar_label` can be applied **in a single line** with list comprehension.

---

## 5️⃣ GroupBy & Numeric Operations

* Only numeric columns can be averaged:

```python
gender_group = df.groupby('gender').mean(numeric_only=True)
```

* Use `.loc` for safe indexing:

```python
female_scores = [gender_group.loc['female', 'average'], gender_group.loc['female', 'math score']]
```

---

## 6️⃣ Grouped Bar Charts

* Shift bars for groups:

```python
X_axis = np.arange(len(categories))
plt.bar(X_axis - 0.2, male_scores, 0.4, label='Male')
plt.bar(X_axis + 0.2, female_scores, 0.4, label='Female')
```

* `-0.2` / `+0.2` offsets bars to avoid overlap.
* Width controls bar thickness.

---

## 7️⃣ Boxplots and Multiple Subplots

* Object-oriented style:

```python
fig, ax = plt.subplots(1, 4, figsize=(16,5))
sns.boxplot(x=df['math score'], color='skyblue', ax=ax[0]); ax[0].set_title('Math Score')
sns.boxplot(x=df['reading score'], color='hotpink', ax=ax[1]); ax[1].set_title('Reading Score')
plt.tight_layout(); plt.show()
```

* Single-line plot calls are cleaner and easier to manage.

---

## 8️⃣ Styling Figures

* Check available styles:

```python
plt.style.available
plt.style.use('fivethirtyeight')  # valid styles
```

* Avoid invalid styles like `'seaborn-talk'`.

---

## 9️⃣ Best Practices Learned

* **Single-line plotting** keeps code compact.
* Use `ax[]` for object-oriented style.
* Always use `numeric_only=True` when doing `.mean()` or `.agg()` on grouped data.
* Use `plt.cm` colormaps for dynamic color scaling.
* Always label axes and plots for clarity.
* Use `plt.tight_layout()` to prevent overlapping in multi-plot figures.

---
---

# 📊 Data Analysis Types & Examples

## 1️⃣ Univariate Analysis

* **Definition:** Analyzing a **single variable** to understand its distribution or characteristics.
* **Example:** Count of students by gender or lunch type.

```python
# Countplot for gender (categorical)
sns.countplot(x='gender', data=df, palette='bright'); plt.title('Gender Count'); plt.show()

# Pie chart for lunch distribution
plt.pie(df['lunch'].value_counts(), labels=df['lunch'].value_counts().index, autopct='%1.1f%%', colors=plt.cm.Set2.colors); plt.title('Lunch Distribution'); plt.show()
```

**Key Idea:** Focus on **one variable at a time**.

---

## 2️⃣ Bivariate Analysis

* **Definition:** Exploring the relationship **between two variables**.
* **Example:** Average scores by gender.

```python
gender_group = df.groupby('gender').mean(numeric_only=True)

X_axis = np.arange(2)
male_scores = [gender_group.loc['male','average'], gender_group.loc['male','math score']]
female_scores = [gender_group.loc['female','average'], gender_group.loc['female','math score']]

plt.bar(X_axis - 0.2, male_scores, 0.4, label='Male')
plt.bar(X_axis + 0.2, female_scores, 0.4, label='Female')
plt.xticks(X_axis, ['Total Average','Math Average'])
plt.ylabel('Marks')
plt.title('Average & Math Scores by Gender')
plt.legend()
plt.show()
```

**Key Idea:** Compare **two variables**, e.g., gender vs scores.

---

## 3️⃣ Multivariate Analysis

* **Definition:** Examining **three or more variables** simultaneously to detect patterns or relationships.
* **Example:** How lunch type and test preparation course affect math scores.

```python
plt.figure(figsize=(12,6))
sns.barplot(x='lunch', y='math score', hue='test preparation course', data=df); plt.title('Math Scores by Lunch & Test Preparation'); plt.show()
```

* You can extend this to reading and writing scores similarly:

```python
sns.barplot(x='lunch', y='reading score', hue='test preparation course', data=df)
sns.barplot(x='lunch', y='writing score', hue='test preparation course', data=df)
```

**Key Idea:** Examine **more than two variables**, e.g., lunch + test prep + scores.

---

### Summary Table

| Analysis Type | Variables | Example Plot                              |
| ------------- | --------- | ----------------------------------------- |
| Univariate    | 1         | Gender countplot, Lunch pie chart         |
| Bivariate     | 2         | Gender vs Average/Math scores bar chart   |
| Multivariate  | 3+        | Lunch vs Test Prep vs Math scores barplot |

---
---