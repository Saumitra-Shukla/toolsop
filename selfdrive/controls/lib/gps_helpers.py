_RHD_REGION_MAP = [ ['AUS', -54.76, -9.23, 112.91, 159.11], \
                    ['IN1', 6.75, 28.10, 68.17, 97.4], \
                    ['IN2', 28.09, 35.99, 72.18, 80.87], \
                    ['IRL', 51.42, 55.38, -10.58, -5.99], \
                    ['JP1', 32.66, 45.52, 137.27, 146.02], \
                    ['JP2', 32.79, 37.60, 131.41, 137.28], \
                    ['JP3', 24.04, 34.78, 122.93, 131.42], \
                    ['NZ', -52.61, -29.24, 166, 178.84], \
                    ['SF', -35.14, -22.13, 16.07, 33.21], \
                    ['UK', 49.9, 60.84, -8.62, 1.77] ]

def is_rhd_region(latitude, longitude):
  for region in _RHD_REGION_MAP:
    if region[1] <= latitude <= region[2] and \
      region[3] <= longitude <= region[4]:
      return True
  return False