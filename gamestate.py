import pyarrow.parquet as pq 

metadata = pq.read_metadata('game_state_frame_data.parquet')

print(metadata)
