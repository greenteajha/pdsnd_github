import time
import pandas as pd
import numpy as np
import calendar

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
    city = input('Input city(chicago, new york city, washington): ')
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input('INVALID INPUT! Input city(chicago, new york city, washington) again: ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Input month(all, january, february, ... , june): ')
    while month.lower() not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input('INVALID INPUT! Input month(all, january, february, ... , june): ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Input day of week(all, monday, tuesday, ... sunday): ')
    while day.lower() not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day = input('INVALID INPUT! Input day of week(all, monday, tuesday, ... sunday): ')

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[pd.to_datetime(df['Start Time']).dt.month == month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        # filter by day of week to create the new dataframe
       
        df = df.loc[pd.to_datetime(df['Start Time']).dt.dayofweek == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Extract out month from start time
#    print(df)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    print("----- MOST COMMON MONTH -----\n")
    print("Most common month is: " + str(calendar.month_name[(df['Start Time'].dt.month).mode()[0]]))
    print("\n")
    

    # TO DO: display the most common day of week
    print("----- MOST COMMON DAY OF WEEK -----\n")
    print("Most common day of the week is: " + str(calendar.day_name[(df['Start Time'].dt.dayofweek).mode()[0]]))
    print("\n")
    

    # TO DO: display the most common start hour
    print("----- MOST COMMON START HOUR -----\n")
    print("Most common start hour of the week is: {}00 Hrs".format(str((df['Start Time'].dt.hour).mode()[0])))
    print("\n")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("----- COMMONLY USED START STATION -----\n")
    print("Most commonly used start station: " + df['Start Station'].mode()[0])
    print("\n")
    

    # TO DO: display most commonly used end station
    print("----- COMMONLY USED END STATION -----\n")
    print("Most commonly used end station: " + df['End Station'].mode()[0])
    print("\n")
    

    # TO DO: display most frequent combination of start station and end station trip
    print("----- MOST FREQUENT START AND END STATION COMBINATION -----\n")
    combi = df.groupby(['Start Station', 'End Station']).size().to_frame('count').reset_index().sort_values(by='count', ascending=False).head(1).values[0]
    print("Start Station: {}\nEnd Station: {}".format(combi[0],combi[1]))
    print("\n")
   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("----- TOTAL TRAVEL TIME -----\n")
    print("Total travel time: {} MINUTES".format(str(df['Trip Duration'].sum()/60)))
    print("\n")
    

    # TO DO: display mean travel time
    print("----- TRAVEL MEAN TIME -----\n")
    print("Mean travel time: {} MINUTES".format(str(df['Trip Duration'].mean()/60)))
    print("\n")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("----- USER TYPE COUNT -----\n")
    uType = (df['User Type'].value_counts()).to_dict()
    for key,value in uType.items():
        print("User Type: {}, Count: {}".format(key,value))
    print("\n")
    
    try:
        # TO DO: Display counts of gender
        print("----- GENDER COUNT -----\n")
        gender = (df['Gender'].value_counts()).to_dict()
        for key,value in gender.items():
            print("Gender: {}, Count: {}".format(key,value))
        print("\n")
    except:
        print("\n")
        print("ERROR! Cannot gather a gender count due to missing 'GENDER' column!")
        print("\n")

    try:
        # TO DO: Display earliest, most recent, and most common year of birth
        # Calculates the earlier year of birth
        print("----- EARLIEST YEAR OF BIRTH -----\n")
        print("Earliest year of birth: {}".format(str(int(df['Birth Year'].dropna(axis=0).sort_values().head(1).values[0]))))
        print("\n")
        # Calculates the recent year of birth
        print("----- MOST RECENT YEAR OF BIRTH -----\n")
        print("Most recent year of birth: {}".format(str(int(df['Birth Year'].dropna(axis=0).sort_values(ascending=False).head(1).values[0]))))
        print("\n")
        # Calculates the most common year of birth
        print("----- MOST COMMON YEAR OF BIRTH -----\n")
        print("Most common year of birth: {}".format(str(int(df['Birth Year'].dropna(axis=0).value_counts().head(1).index[0]))))
        print("\n")
    except:
        print("\n")
        print("ERROR! Cannot gather a birth year data count due to missing 'BIRTH YEAR' column!")
        print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    
    rData = input("Would you like to see the raw data input? (yes or no): ").lower()
    while rData != 'yes' and rData != 'no':
        rData = input("ERROR INPUT! Would you like to see the raw data input? (yes or no): ").lower()
    repeat = "yes"
    n = 5
    if rData == "yes":
        while repeat != "no":
            rDataDict = df.iloc[n-5:n].to_dict()
            print("\n")
            for i in range(n-5, n):
                print("Record Number: {}".format(i+1))
                print("Start Time: {}".format(rDataDict["Start Time"][i]))
                print("End Time: {}".format(rDataDict["End Time"][i]))
                print("Trip Duration: {}".format(rDataDict["Trip Duration"][i]))
                print("Start Station: {}".format(rDataDict["Start Station"][i]))
                print("End Station: {}".format(rDataDict["End Station"][i]))
                print("User Type: {}".format(rDataDict["User Type"][i]))
                if rDataDict.get('Gender') is not None and rDataDict.get('Birth Year') is not None:
                    print("Gender: {}".format(rDataDict["Gender"][i]))
                    print("Birth Year: {}".format(rDataDict["Birth Year"][i]))
                print("\n")
            repeat = input("Would you like to see another 5 raw data? (yes or no): ")
            while repeat != "yes" and repeat != "no":
                repeat = input("ERROR INPUT! Would you like to see another 5 raw data? (yes or no): ")
            if repeat == "yes":
                n += 5

                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

