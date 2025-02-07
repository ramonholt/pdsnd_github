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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("What city would you like to analyze: Chicago, New York City or Washington?  For all, specify All. ").title()
        if city.title() not in("Chicago", "New York City", "Washington", "All"):
            print("I don't understand your option.  Valid responses are: Chicago, New York City, Washington or All")
            continue
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("What month would you like to analyze: January, February, March, April, May or June?  For all, specify All. ").title()
        if month.title() not in("January", "February", "March", "April", "May", "June", "All"):
            print("I don't understand your option.  Valid responses are: January, February, March, April, May, June or All")
            continue
        break 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What day of the week would you like to analyze: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday?  For all, specify All. ").title()        
        if day.title() not in("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "All"):
            print("I don't understand your option.  Valid responses are: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday or All")
            continue
        break

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
    #print(city)
    #print(city.lower().replace(' ','_') + '.csv')
    if city in ['Chicago', 'New York City', 'Washington']:
        #print(city.lower().replace(' ','_') + '.csv')
        #thecity = city.lower().replace(' ','_') + '.csv'
        #print(thecity)
        df = pd.read_csv(city.lower().replace(' ','_') + '.csv')
        #df = pd.read_csv(thecity)
    # if All is selected combine all files into one dataframe
    elif city == 'All':
        dfch = pd.read_csv('chicago.csv')
        dfny = pd.read_csv('new_york_city.csv')
        dfwa = pd.read_csv('washington.csv')        
        #df = pd.concat([dfch, dfny, dfwa], axis=1)
        df = pd.concat([dfch, dfny, dfwa], axis=0)
        #print(df.columns)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] =  pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month    
    df['month'] = pd.to_datetime(df['Start Time']).dt.strftime('%B')
    print('Most Common Month: {}'.format(df['month'].mode()[0]))    

    # TO DO: display the most common day of week
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.strftime('%A')
    print('Most Common Day of the Week: ' + df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    #print(df['hour'].head())
    print('Most Common Hour of the day: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #df['hour'] = df['Start Time'].dt.hour    
    print('Most Common Start Station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Common End Station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End'] = df['Start Station'] + ' to ' +df['End Station']
    print('Most Common combination of Start and End Station: ', df['Start and End'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Time: " + str((pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()))
    #print("Total Travel Time: " + str(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])))

    # TO DO: display mean travel time
    print("Mean Travel Time: " + str((pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Types: \n ")
    print(str(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    print("\nGender Info: \n ")
    if df.get('Gender') is not None:
        #dfnoNan = df.dropna(subset=['Gender', 'Birth Year'])
        dfnoNanG = df.dropna(subset=['Gender'])
        print(dfnoNanG['Gender'].value_counts())        
    else:
        print("No Gender information available.")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if df.get('Birth Year') is not None:        
        dfnoNanBY = df.dropna(subset=['Birth Year'])
        print("\n Earliest Birth Year: " + str(int(dfnoNanBY['Birth Year'].min())))
        print("\n Most Recent Birth Year: " + str(int(dfnoNanBY['Birth Year'].max())))
        print("\n Most Common Birth Year: ")
        print("Mode: " + str(int(df['Birth Year'].mode())))
        print("Mean: " + str(int(df['Birth Year'].mean())))
    else:
        print("No Gender information available.")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def chunker(df, size):
    i = 0
        for i in range(0, len(df), size):
        print(df[i:i+size])
        i += size        
        theinput = input("Would you like more RAW data?")        
        if theinput.lower() != 'yes':            
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw = input('\nWould you like to see the RAW data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            chunker(df, 5)            
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
