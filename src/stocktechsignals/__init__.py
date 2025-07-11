"""
StockTechSignals Package

A Python tool for real-time stock data analysis and technical signal generation 
using first principles approach to market dynamics.

Main Classes:
    StockAnalyzer: Core analysis engine
    TechnicalIndicators: Technical analysis indicators
    SignalGenerator: Trading signal generation
    DataFetcher: Market data acquisition
    ChartVisualizer: Chart and graph generation

Example Usage:
    from stocktechsignals import StockAnalyzer
    
    analyzer = StockAnalyzer()
    signals = analyzer.analyze_stock("AAPL")

Created with Comet Assistant
"""

__version__ = "0.1.0"
__author__ = "StockTechSignals Development Team"
__email__ = "info@stocktechsignals.com"
__description__ = "Real-time stock analysis using first principles technical analysis"

# Import main classes for easy access
from .analyzer import StockAnalyzer, AnalysisResult, BuySignal, SellSignal

# Import modules for advanced usage
from . import data_fetcher
from . import indicators 
from . import signals
from . import visualizer

# Package level exports
__all__ = [
    'StockAnalyzer',
    'AnalysisResult', 
    'BuySignal',
    'SellSignal',
    'data_fetcher',
    'indicators',
    'signals', 
    'visualizer'
]

# Package configuration
DEFAULT_CONFIG = {
    'timeframe': '1d',
    'lookback_period': 30,
    'volume_threshold': 1.5,
    'confidence_threshold': 0.7,
    'max_positions': 10
}

# Initialize package logger
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
