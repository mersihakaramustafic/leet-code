# Calculate Median booking_value per booking_date

import pandas as pd
import numpy as np

# Defining bookings DataFrame
bookings = pd.DataFrame({
    'booking_id': [1, 2, 3, 4, 5, 6],
    'user_id': [101, 102, 101, 103, 104, 102],
    'booking_value': [100, 200, 150, 300, 250, 180],
    'booking_date': pd.to_datetime(['2025-01-01', '2025-01-01', '2025-01-02', '2025-01-02', '2025-01-02', '2025-01-03'])
})

# Group by booking_date and calculate median using pandas
median_per_day_p = bookings.groupby('booking_date')['booking_value'].median().reset_index()

print(median_per_day_p)

# Group by booking_date and calculate median using numpy
median_per_day_n = bookings.groupby('booking_date')['booking_value'].apply(lambda x: np.median(x)).reset_index()

print(median_per_day_n)
