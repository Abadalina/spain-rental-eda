# Spain Rental EDA — Madrid Short-Term Rental Market

Exploratory data analysis of Madrid's short-term rental market using real **Inside Airbnb** data.

---

## Goal

Answer key questions about the Madrid rental market:

- What is the average nightly price in Madrid?
- Which neighbourhoods are the most expensive and most affordable?
- How does accommodation type affect price?
- What is the relationship between price, capacity, and reviews?

---

## Project structure

```
spain-rental-eda/
├── data/
│   └── raw/              ← place the downloaded CSV here
├── notebooks/
│   └── 01_eda_madrid_airbnb.ipynb   ← main notebook
├── src/
│   └── utils.py          ← cleaning and visualisation helpers
├── outputs/
│   └── figures/          ← auto-generated charts
├── requirements.txt
└── README.md
```

---

## Data

Data comes from **[Inside Airbnb](http://insideairbnb.com/get-the-data/)**, an independent project that collects public Airbnb data.

**How to download:**
1. Go to http://insideairbnb.com/get-the-data/
2. Search for **Madrid, Spain**
3. Download `listings.csv.gz` (the detailed file)
4. Place it in `data/raw/listings.csv.gz`

---

## Installation & usage

```bash
# Clone the repository
git clone https://github.com/Abadalina/spain-rental-eda.git
cd spain-rental-eda

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch the notebook
jupyter notebook notebooks/01_eda_madrid_airbnb.ipynb
```

---

## Key findings

| Finding | Detail |
|---------|--------|
| Median price | ~X € per night for an entire apartment |
| Dominant type | Entire homes/apartments (~X% of listings) |
| Most expensive neighbourhood | Recoletos / Cortes |
| Variable most correlated with price | Capacity (accommodates) |

> Update this table with real values after running the notebook.

---

## Visualisations included

- Price distribution (histogram + boxplot)
- Price by accommodation type (violin plot)
- Top neighbourhoods by listings and by price
- Correlation matrix
- Interactive price heatmap with Folium
- Scatter map with Plotly

---

## Tech stack

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.2-150458)
![Plotly](https://img.shields.io/badge/Plotly-5.22-3F4F75)
![Folium](https://img.shields.io/badge/Folium-0.16-77B829)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13-4C72B0)

---

## Part of the Madrid Housing Portfolio

| # | Project | Description |
|---|---------|-------------|
| 1 | **spain-rental-eda** | Exploratory data analysis ← you are here |
| 2 | [housing-price-ml](https://github.com/Abadalina/housing-price-ml) | ML price prediction |
| 3 | [rental-price-forecast](https://github.com/Abadalina/rental-price-forecast) | Time series forecasting |
| 4 | [airbnb-reviews-nlp](https://github.com/Abadalina/airbnb-reviews-nlp) | NLP sentiment & topic analysis |
| 5 | [housing-price-app](https://github.com/Abadalina/housing-price-app) | Streamlit deployment |

---

## Author

**Alejandro Abadal** — Data Science Student, UOC
[LinkedIn](#) · [GitHub](https://github.com/Abadalina)

---

*Data for educational purposes. Source: Inside Airbnb.*
