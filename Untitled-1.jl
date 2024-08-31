
for day_summary in weather_data:
        convert_date(day_summary[0])
        formatted_date = convert_date(day_summary[0])
        min_num = find_min(day_summary[1])
        value = min_num[0]
        max_num = find_max(day_summary[1])
        value = max_num[0]
return f"---- {formatted_date} ---- \n Minimum Temperature: {value}{format_temperature} \n Maximum Temperature: {max_num}{format_temperature}"