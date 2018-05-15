import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ""
    while city.lower() not in CITY_DATA:
        city = input("Enter one of the following cities by typing in the name.(chicago, new york city, washington)\n-->")
        if city is not "" and city.lower() not in CITY_DATA:
            print("Please select from the suggested cities and type the city name in below.")

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ""
    while month.lower() not in months:
        month = input("Enter the month you are interested in or select all, e.g all, january, february, ..., june\n-->")
        if month is not "" and month.lower() not in months:
            print("Please select from the suggested months and type the month in below.")

    # get user input for day of week (all, monday, tuesday, ... ,sunday)
    weekday = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ""
    while day.lower() not in weekday:
        day = input("Enter the day you are interested in or select all, e.g all, monday, tuesday, ... ,sunday\n-->")
        if day.lower() is not "" and day.lower() not in weekday:
            print("Please select from the suggested days and type the day in below.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # print(df.head())
    # display the most common month
    popular_month = df['month'].value_counts()
    # print("count",popular_month)
    if popular_month.count() == 1:
        print("\tThere is a filter on the month.\n\tTo find the most popular month run again and select 'all' months.")
        print("\tThe month selected is: {}\n".format(months[popular_month.idxmax()].title()))
    else:
        print("\tThe most popular month is: {}\n".format(months[popular_month.idxmax()].title()))

    # display the most common day of week
    popular_day = df['day_of_week'].value_counts()
    # print("counts", popular_day)
    if popular_day.count() == 1:
        print("\tThere is a filter on the day.\n\tTo find the most popular day run again and select 'all' days.")
        print("\tThe day selected is: {}\n".format(popular_day.idxmax()))
    else:
        print("\tThe most popular day is: {}\n".format(popular_day.idxmax()))

    # display the most common start hour
    popular_start_hour = df['Start Time'].dt.hour.value_counts()
    # print("hour",popular_start_hour)
    print("\tThe most popular start hour is: {}".format(popular_start_hour.idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
