# Tweet-Heat: Dynamic Heatmap Visualization of Tweets

Welcome to Tweet-Heat, a cutting-edge project designed to visualize the pulse of the world through tweets. Born out of the HackED-beta competition, Tweet-Heat uses real-time tweet locations to generate interactive heatmaps, revealing fascinating patterns of social media activity across the globe.

What our program does is it crawls through Twitter data and receives live tweets from all over North America. Of all these tweets collected, roughly 10 percent have location data with them. The program then puts all of these latitude and longitude coordinate points on a map, and generates a heat map where the highest traffic locations around North America are highlighted.

## Features

- **Real-Time Visualization**: See the world's conversations unfold with live updates to tweet locations.
- **Interactive Heatmaps**: Navigate through interactive maps to see where discussions are heating up.
- **Customizable Views**: Adjust the parameters of your heatmap for customized data exploration.
- **Geospatial Insights**: Harness the power of geospatial analysis to uncover trends and insights from Twitter data.

## Getting Started

### Prerequisites

Before diving in, make sure you have:

- Python 3.x installed on your system.
- Folium for mapping.
- SQLite3 for database management.

### Installation

1. Clone the Tweet-Heat repository:

```bash
git clone https://github.com/mjbraun95/Tweet-Heat.git
cd Tweet-Heat
```

2. Install necessary Python libraries:
```bash
python3 -m pip install folium sqlite3
```

3. Run the following command:
```bash
python3 mapGen.py
```
This will process the latest tweet data and produce a heatmap visualization in static/heatMap.html. Open this file in any web browser to view your interactive heatmap.