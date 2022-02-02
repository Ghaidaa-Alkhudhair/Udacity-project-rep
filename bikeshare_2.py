#Ghaida Alkhudhair
import time
import pandas as pd
import numpy as np
try:
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
except:
    print("An EXCEPTION OCCURE PLEASE MAKE SURE YOU YOU HAVE THE CVS FILE IN THE DIRECTORY")

def get_filters():
    #inside method get_filters()
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city_list=['chicago', 'new york city', 'washington']
    day_list=['saturday','sunday','monday','tuesday','wednesday','thursday','all']
    month_list=['january','february','march','april','may','june','july','all']
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Please enter one of these cities : chicago, new york city, washington ").lower()

    while city not in city_list:
        city=input("You entered WRONG data ! please try again and enter one of these cityies :chicago, new york city, washington ").lower()


    # get user input for month (all, january, february, ... , june)
    month=input("please enter all or specify month to filter data : ").lower()
    while month not in month_list:
        month=input("You entered WRONG data ! please try again and enter one of these months: january,february,march,april,may,june,july OR all ").lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("please enter all or a weekday to filter data : ").lower()
    while day not in day_list:
        day=input("You entered WRONG data ! please try again and enter one of these day: saturday,sunday,monday,tuesday,wednesday,thursday OR all ").lower()


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
## This method is the same as the problem#3 since they all ask for the same thing.
    # load data file into a dataframe
    try:
        df = pd.read_csv(CITY_DATA[city])
    except:
        print("An EXCEPTION OCCURE PLEASE MAKE SURE YOU YOU HAVE THE CVS FILE IN THE DIRECTORY")
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

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
## before function time_stats(df):
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month=df['month'].mode()[0]
    print("The most common month is: ")
    print(common_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    comoon_day=df['day_of_week'].mode()[0]
    print("The mosy common day is: ")
    print(comoon_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print("The most common hour is: ")
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print("The most commonly used start station is:  ")
    print(common_start_station)


    # display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print("The most commonly used end station is: ")
    print(common_end_station)

    # display most frequent combination of start station and end station trip
    common_start_end=common_start_station+ ' '+ common_end_station
    #common_start_end=df['frequent_start_end'].mode()[0]
    print("The most frequent combination of start station and end station trip is: ")
    print(common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time=df['Trip Duration'].sum()
    print("The total travel time is: ")
    print(total_time)

    # display mean travel time
    mean_time=df['Trip Duration'].mean()
    print("The average travel time is: ")
    print(mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    cout_of_usere=df['User Type'].value_counts()
    print("The counts of user type is: ")
    print(cout_of_usere)

    # Display counts of gender
    if 'Gender' in df.columns: # Since washington does not have Gender column then it does not have a year of birth column too , so I just used if steatement to check for the gender because it does the both.

        count_of_gender=df['Gender'].value_counts()
        print("the counts of gender is: ")
        print(count_of_gender)
        earliest=df['Birth Year'].max()
        print("The earliest year of birth is: ")
        print(earliest)
        recent=df['Birth Year'].min()
        print("The most recent year of birth is: ")
        print(recent)
        common_year_of_birth=df['Birth Year'].mode()[0]
        print("The most common year of birth is: ")
        print(common_year_of_birth)
    else:
        print("The city you have chosen does not have Gender column")
        print("The city you have chosen does not have Birth year column")



    # Display earliest, most recent, and most common year of birth
    #if city!='washington' :

    #if 'Birth year' in df.columns:
        #recent=df['Birth Year'].min()
        #print("The most recent year of birth is: ")
        #print(recent)
    #if 'Birth year' in df.columns:
        #common_year_of_birth=df['Birth Year'].mode()[0]
        #print("The most common year of birth is: ")
        #print(common_year_of_birth)
    #else:
        #print("The city you have chosen does not contain year of birth column!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    start_loc= 0
    askk=input("Do you want to display the first 5 rows?? Please enter yes or no ").lower()

    if askk=='yes':
        while (askk=='yes') :
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5
            askk=input("Do you want to see the next 5 rows ?? Please enter yes or no ").lower()






def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df) ### the function that I added
        print('-'*40)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
