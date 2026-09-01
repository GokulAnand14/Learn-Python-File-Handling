# 11. Custom Binary Format Parser (Hard)
import struct

def parse_sensor_data(filepath):
    # Format: < (little-endian), i (int, 4 bytes), f (float, 4 bytes), i (int, 4 bytes)
    record_format = '<ifi'
    record_size = struct.calcsize(record_format)
    
    max_temp = float('-inf')
    
    with open(filepath, 'rb') as f:
        while True:
            raw_record = f.read(record_size)
            if len(raw_record) < record_size:
                break
                
            sensor_id, temp, timestamp = struct.unpack(record_format, raw_record)
            
            if sensor_id == 2:
                if temp > max_temp:
                    max_temp = temp
                    
    print(f"Max temperature for sensor 2 is: {max_temp:.2f}")

if __name__ == '__main__':
    parse_sensor_data('../data/sensor_data.bin')
