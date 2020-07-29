for hours in range(24):
    # за всеки един час искаме да се завъртят всички минути
    for minutes in range(60):
        # за всяка минута искаме да се завъртят всички секунди
        print(f'{hours}:{minutes}')
        for sec in range(60):
            print(f'{hours:02d}:{minutes:02d}:{sec:02d}')