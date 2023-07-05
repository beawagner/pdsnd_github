import time
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 200)

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input('\nEnter the name of the city you want to learn more about: \n').lower()
        if city not in ("chicago","new york","washington","new york city"):
            print('\nError! Please enter one of these cities: Chicago, New York/New York City, Washington\n')
        else: break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nEnter the name of the month to filter by, or type "all" to apply no month filter (all, january, february,...): \n').lower()
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        if month not in months:
            print('\nError! Please enter the month name again!\n')
        else: break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nEnter the name of the day to filter by, or type "all" to apply no day filter (all, monday, tuesday,...): \n').lower()
        day_name = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day not in day_name:
            print('\nError! Please enter the day name again!\n')
        else: break
    
    if city == "new york":
        city = 'new york city'
    
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek + 1

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = weekday.index(day) + 1
        df = df[df['day_of_week'] == day]
    
    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_name = months[popular_month - 1].title()
    
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_name = weekday[popular_day - 1].title()

    # TO DO: display the most common start hour
    popular_time = df['Start Time'].dt.hour.mode()[0]
    
    if len(set(df['month'].values)) != 1:
        print('\nThe most popular month: \n{}'.format(month_name))
    
    if len(set(df['day_of_week'].values)) != 1:
        print('\nThe most popular day: \n{}'.format(day_name))
        
    print('\nThe most popular start hour: \n{}'.format(popular_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df.apply(lambda x: '%s - %s' % (x['Start Station'], x['End Station']), axis = 1)
    popular_comb = df['trip'].mode()[0]
    
    print('The most popular start station: \n{}'.format(popular_start))
    print('\nThe most popular end station: \n{}'.format(popular_end))
    print('\nThe most popular trip: \n{}'.format(popular_comb))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    
    print('The total time traveled: \n{}'.format(total_time))
    print('\nThe average time traveled: \n{}'.format(avg_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts by User Types: \n{}'.format(user_types))

    # TO DO: Display counts of gender
     
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print('\nCounts by Gender: \n{}'.format(gender_count))
    else: print('\nThere is no gender data to show.')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        oldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('\nThe earliest year of birth: {}'.format(oldest))
        print('\nThe most recent year of birth: {}'.format(youngest))
        print('\nThe most common year of birth: {}'.format(common_year))
    else: print('\nThere is no birth data to show.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Displays the first 5 rows of the table """
    i = 0
    while (i + 5) <= df.shape[0]:
        yield df.iloc[i:(i + 5), :]
        i += 5
        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)    
        
        for df in display_data(df):             
            data = input('\nWould you like to see the raw data? Enter yes or no.\n')
            if data.lower() == 'yes':
                print(df)
                continue
            else: break                

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()