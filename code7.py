import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ("chicago", "new york", "washington")
    while True:
         city = input( "Which of these cities do you want to know about It: chicago, new york or washington? \n> " ).lower()
         if city in cities:
             break
         if city not in cities:
             print("Please enter an available value, see Question Options")


    # TO DO: get user input for month (all, january, february, ... , june)
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    months = ["january" , "february" , "march" , "april" , "may" , "june" , "all"]
    while True:
      month = input("Now you have to enter a month to get some months result \n> ").lower()
      if month in months:
           break
      if month not in months:
            print( "Please enter an available value like : january , february , march , april , may , june or choose all " ).lower()
      if month != "all" :
        months = ["january" , "february" , "march" , "april" , "may" , "june" ]
        month = months.index(month) + 1

        df = df[df['month'] == month]


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday" , "all" ]
    while True:
      day = input("Now you have to enter a day to get some days result \n> ").lower()
      if day in days:
           break
      if day not in days:
            print("Please enter an available value like : sunday , monday , tuesday , wednesday , thursday , friday , saturday Or, choose all " )
      if day != "all" :
        df = df[df['day_of_week'] == day.title()]
    print("-" * 40)
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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print( '''
Calculating The Most Frequent Times of Travel...
''')
    start_time = time.time()

    # TO DO: display the most common month

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print ('the most common month : ', most_common_month)

    # TO DO: display the most common day of week

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.weekday_name
    most_common_day = df['day'].mode()[0]
    print ('the most common day of week is : ', most_common_day)

    # TO DO: display the most common start hour

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print ('the most common start hour : ', most_common_start_hour)

    print( '\nThis took %s seconds.' % (time.time() - start_time))
    print ('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print ('''
Calculating The Most Popular Stations and Trip...
''')
    start_time = time.time()

    # TO DO: display most commonly used start station

    commonly_used_start_station = df['Start Station'].mode()[0]
    print ('The most commonly used start station:', most_commonly_used_start_station)

    # TO DO: display most commonly used end station

    commonly_used_end_station = df['End Station'].mode()[0]
    print ('The most commonly used end station:', most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    df['combination_start_and_end'] = df['End Station'] + df['Start Station']
    print ('The most frequent combination of start station and end station trip:' , df['combination_start_and_end'].mode()[0])

    print( '\nThis took %s seconds.' % (time.time() - start_time))
    print( '-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print ('''
Calculating Trip Duration...
''')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print ('The total travel time :', total_travel_time)

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print ('The mean travel time :', mean_travel_time)

    print ('\nThis took %s seconds.' % (time.time() - start_time))
    print ('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print( '''
Calculating User Stats...
''')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print ('the counts of user types : ', user_types)

    # TO DO: Display counts of gender

    if 'Gender' and 'Birth Year'in df :
     gender = df['Gender'].value_counts()
     print ('the counts of gender of users : ', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
     print ('The earliest year of birth : ', df['Birth Year'].min())
     print ('The most recent year of birth : ', df['Birth Year'].max())
     print ('The most common year of birth : ', df['Birth Year'].mode())
    else:
        print ('the Birth year information and gender for users is not available for washington city ')



    print ('\nThis took %s seconds.' % (time.time() - start_time))
    print ('-' * 40)

def more_rows (df) :
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no \n").lower()
    start_loc = 0
    if view_data == "yes" :
        more_rowss = True
    else:
        more_rowss = False


    while (more_rowss):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue? Enter yes or no \n").lower()
        if view_display == "yes" :
            more_rowss = True
        else:
            more_rowss = False


def main():
    while True:
        (city, month, day) = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_rows (df)


        restart = \
            input('''
Would you like to restart? Enter yes or no.
''')
        if restart.lower() != 'yes':
            break


if __name__ == '__main__':
    main()
