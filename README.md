# StockTechSignals

A Python tool for real-time stock data analysis and technical signal generation using first principles approach to market dynamics.

## What This Tool Does

StockTechSignals is a comprehensive Python application that:

- **Fetches Real-Time Stock Data**: Connects to financial APIs to retrieve live market data including price, volume, and other key metrics
- **Applies First Principles Technical Analysis**: Uses fundamental market dynamics rather than complex indicators to analyze price movements
- **Generates Buy/Sell Signals**: Produces actionable trading signals based on systematic analysis of market conditions
- **Provides Clear Visualizations**: Creates charts and graphs to help understand market trends and signal generation

## First Principles Approach

This tool is built on core market principles rather than relying on complex technical indicators:

### Market Dynamics Foundation
- **Supply and Demand**: Analyzing volume patterns and price action to understand underlying market forces
- **Trend Identification**: Using price structure and momentum to identify market direction
- **Support and Resistance**: Identifying key price levels where buying and selling pressure converge
- **Volume Analysis**: Understanding the relationship between price movements and trading volume

### Basic Indicators Used
- **Moving Averages**: Simple and exponential moving averages for trend identification
- **Volume Indicators**: Volume-weighted average price (VWAP) and volume trends
- **Momentum Oscillators**: RSI and basic momentum calculations
- **Price Action Patterns**: Candlestick patterns and chart formations

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jigaraero/StockTechSignals.git
   cd StockTechSignals
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**:
   - Copy `config/config_template.py` to `config/config.py`
   - Add your financial data API keys (Alpha Vantage, Yahoo Finance, etc.)
   ```python
   API_KEY = "your_api_key_here"
   ```

## Usage

### Basic Usage

```python
from stocktechsignals import StockAnalyzer

# Initialize analyzer
analyzer = StockAnalyzer()

# Analyze a stock
signals = analyzer.analyze_stock("AAPL")

# Get buy/sell recommendations
for signal in signals:
    print(f"Signal: {signal.action} at {signal.price} - Confidence: {signal.confidence}")
```

### Advanced Usage

```python
# Custom analysis with specific parameters
analyzer = StockAnalyzer(
    timeframe="1d",
    lookback_period=30,
    volume_threshold=1.5
)

# Batch analysis
stocks = ["AAPL", "GOOGL", "MSFT", "TSLA"]
results = analyzer.batch_analyze(stocks)

# Generate report
analyzer.generate_report(results, output_format="html")
```

### Command Line Interface

```bash
# Analyze single stock
python -m stocktechsignals analyze AAPL

# Real-time monitoring
python -m stocktechsignals monitor --stocks AAPL,GOOGL,MSFT

# Generate batch report
python -m stocktechsignals report --input stocks.txt --output report.html
```

## Project Structure

```
StockTechSignals/
├── src/
│   ├── stocktechsignals/
│   │   ├── __init__.py
│   │   ├── analyzer.py          # Core analysis engine
│   │   ├── data_fetcher.py      # Data acquisition module
│   │   ├── indicators.py        # Technical indicators
│   │   ├── signals.py           # Signal generation logic
│   │   └── visualizer.py        # Chart and graph generation
│   └── tests/
├── config/
│   ├── config_template.py       # Configuration template
│   └── indicators_config.py     # Indicator parameters
├── docs/
│   ├── examples/               # Usage examples
│   ├── api_reference.md        # API documentation
│   └── signal_explanations.md  # Signal methodology
├── requirements.txt            # Python dependencies
├── setup.py                   # Package setup
├── README.md                  # This file
└── .gitignore                 # Git ignore rules
```

## Documentation

### Example Outputs

#### Signal Analysis Output
```
=== AAPL Analysis Results ===
Timestamp: 2025-07-11 15:08:00
Current Price: $195.23

Signals Generated:
1. BUY Signal - Confidence: 85%
   - Reason: Price broke above 20-day MA with strong volume
   - Entry Point: $194.50
   - Stop Loss: $188.75
   - Target: $205.00

2. Volume Confirmation - Strength: High
   - Current Volume: 45.2M (150% of avg)
   - VWAP: $194.12 (Price above VWAP)
```

#### Chart Visualization
The tool generates interactive charts showing:
- Price action with moving averages
- Volume analysis
- Signal entry/exit points
- Support and resistance levels

### Code Explanations

#### Signal Generation Logic
```python
def generate_buy_signal(self, data):
    """
    Generate buy signal based on first principles:
    1. Price action: Higher highs and higher lows
    2. Volume confirmation: Above average volume
    3. Momentum: Positive price momentum
    4. Support: Price holding above key support level
    """
    price_trend = self.analyze_price_trend(data)
    volume_confirmation = self.check_volume_confirmation(data)
    momentum = self.calculate_momentum(data)
    
    if all([price_trend, volume_confirmation, momentum > 0]):
        return BuySignal(
            confidence=self.calculate_confidence(data),
            entry_price=data['close'][-1],
            stop_loss=self.calculate_stop_loss(data),
            target=self.calculate_target(data)
        )
    return None
```

#### Data Processing Pipeline
```python
def process_market_data(self, symbol, timeframe='1d'):
    """
    Process raw market data through analysis pipeline:
    1. Data validation and cleaning
    2. Technical indicator calculation
    3. Pattern recognition
    4. Signal generation
    5. Risk assessment
    """
    raw_data = self.fetch_data(symbol, timeframe)
    clean_data = self.clean_data(raw_data)
    indicators = self.calculate_indicators(clean_data)
    patterns = self.identify_patterns(clean_data)
    signals = self.generate_signals(clean_data, indicators, patterns)
    
    return AnalysisResult(signals, indicators, patterns)
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational and informational purposes only. It should not be considered as financial advice. Always conduct your own research and consult with qualified financial advisors before making investment decisions.

---

*Created with Comet Assistant*
