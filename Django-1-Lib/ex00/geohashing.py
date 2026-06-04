import sys
from antigravity import geohash


class UsageError(Exception):
    pass


class CoordinateError(Exception):
    pass


class DateError(Exception):
    pass


def validate_datedow(datedow):
    parts = datedow.split("-")
    if len(parts) != 4:
        raise DateError("Date must be in the format YYYY-MM-DD-DOW")
    year, month, day, dow = parts
    if not (int(year) > 0 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31):
        raise DateError("Invalid date values")
    try:
        float(dow)
    except ValueError:
        raise DateError("DOW value must be a number")


def validate_coordinates(lat, lon):
    if not (-90 <= lat <= 90):
        raise CoordinateError("Latitude must be between -90 and 90")
    if not (-180 <= lon <= 180):
        raise CoordinateError("Longitude must be between -180 and 180")


def parse_args(argv):
    if len(argv) != 4:
        raise UsageError("Usage: geohashing.py <lat> <lon> <YYYY-MM-DD-DOW>")
    try:
        lat = float(argv[1])
        lon = float(argv[2])
    except ValueError:
        raise UsageError("Latitude and longitude must be numbers")
    return lat, lon, argv[3]


def main():
    try:
        lat, lon, datedow = parse_args(sys.argv)
        validate_coordinates(lat, lon)
        validate_datedow(datedow)
        geohash(lat, lon, datedow.encode("utf-8"))
    except (UsageError, CoordinateError, DateError) as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
