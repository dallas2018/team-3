import * as React from 'react';
import { Text, View, StyleSheet } from 'react-native';

import { createBottomTabNavigator} from 'react-navigation';

import { Ionicons } from '@expo/vector-icons'

import Explore from './screens/Explore'
import Charity from './screens/Charity'
import Sell from './screens/Sell'
import Account from './screens/Account'

export default createBottomTabNavigator({
  Explore:{
    screen: Explore,
    navigationOptions: {
      tabBarLabel: 'EXPLORE',
      tabBarIcon: ({ tintColor }) => (
        <Ionicons name= "ios-search-outline" size={25} color={tintColor} />
      )
    }
  },
  Charity: {
    screen: Charity,
    navigationOptions: {
      tabBarLabel: 'CHARITY',
      tabBarIcon: ({ tintColor }) => (
        <Ionicons name= "ios-heart-outline" size={25} color={tintColor} />
      )
    }
  },
  Sell: {
    screen: Sell,
    navigationOptions: {
      tabBarLabel: 'SELL',
      tabBarIcon: ({ tintColor }) => (
        <Ionicons name= "ios-pricetag-outline" size={25} color={tintColor} />
      )
    }
  },
  Account: {
    screen: Account,
    navigationOptions: {
      tabBarLabel: 'ACCOUNT',
      tabBarIcon: ({ tintColor }) => (
        <Ionicons name= "ios-contact-outline" size={25} color={tintColor} />
      )
    }
  }
},{
  tabBarOptions: {
    activeTintColor: 'blue',
    inactiveTintColor: 'grey',
    style: {
      backgroundColor: 'white',
      elevation: 5
    }
  }
})

