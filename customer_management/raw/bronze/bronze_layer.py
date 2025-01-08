"""
Module to extract data for the bronze layer
"""

import logging
import pandas as pd

from customer_management.database.settings import engine, HANDLER_CONNECTION

logger = logging.getLogger(__name__)

def bronze_customers():
    """
    Extracts raw data from the customers table.
    """
    logger.info("Starting bronze layer...")
    
    if not engine or not HANDLER_CONNECTION:
        logger.error("Database connection settings not properly configured")
        return pd.DataFrame()
    
    query = """
        SELECT 
            id,
            name,
            email,
            contact,
            country,
            state,
            city,
            neighborhood,
            created_at
        FROM customers
        ORDER BY created_at DESC
    """
    
    try:
        with engine.connect() as conn:
            df = pd.read_sql(query, conn, params=None, coerce_float=True, parse_dates=['created_at'])
            if df.empty:
                logger.warning("No data retrieved from database")
            else:
                logger.info(f"Bronze layer - DataFrame shape: {df.shape}")
                logger.info(f"Bronze layer - Columns: {df.columns.tolist()}")
            return df
    except Exception as e:
        logger.error(f"Error reading from database: {str(e)}")
        logger.error(f"Connection string: {HANDLER_CONNECTION}")
        return pd.DataFrame()
