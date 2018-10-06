import React, { Component } from 'react';
import {
  Text,
  View,
  StyleSheet,
  SafeAreaView,
  TextInput,
  Platform,
  StatusBar,
  ScrollView,
  Image,
  Dimensions,
} from 'react-native';

import { Ionicons } from '@expo/vector-icons';
import Category from './components/Explore/Category';

import Item from './components/Explore/Item';

const { height, width } = Dimensions.get('window');
class Explore extends Component {
  constructor(props) {
    super(props);
    this.state = {
      products: [
        { name: 'Item 1', type: 'Category 1', price: 82, rating: 4 },
        { name: 'Item 2', type: 'Category 2', price: 92, rating: 3 },
        { name: 'Item 4', type: 'Category 1', price: 42, rating: 5 },
        { name: 'Item 1', type: 'Category 1', price: 82, rating: 4 },
        { name: 'Item 2', type: 'Category 2', price: 92, rating: 3 },
        { name: 'Item 4', type: 'Category 1', price: 42, rating: 5 },
        { name: 'Item 1', type: 'Category 1', price: 82, rating: 4 },
        { name: 'Item 2', type: 'Category 2', price: 92, rating: 3 },
        { name: 'Item 4', type: 'Category 1', price: 42, rating: 5 },
      ],
    };
  }
  componentWillMount() {
    this.startHeaderHeight = 80;
    if (Platform.OS == 'android') {
      this.startHeaderHeight = 100 + StatusBar.currentHeight;
    }
  }

  render() {
    return (
      <SafeAreaView style={{ flex: 1 }}>
        <View style={{ flex: 1 }}>
          <View
            style={{
              height: this.startHeaderHeight,
              backgroundColor: 'white',
              borderBottomWidth: 1,
              borderBottomColor: '#dddddd',
            }}>
            <View
              style={{
                flexDirection: 'row',
                padding: 10,
                backgroundColor: 'white',
                marginHorizontal: 20,
                shadowOffset: { width: 0, height: 0 },
                shadowColor: 'black',
                shadowOpacity: 0.2,
                elevations: 1,
                marginTop: Platform.OS == 'android' ? 30 : null,
              }}>
              <Ionicons name="ios-search" size={20} />
              <TextInput
                underlineColorAndroid="transparent"
                placeholder="   Search"
                placeholderTextColor="grey"
                style={{
                  flex: 1,
                  fontWeight: '700',
                  backgroundColor: 'white',
                }}
              />
            </View>
          </View>

          <ScrollView scrollEventThrottle={16}>
            <View style={{ marginTop: 40 }}>
              <Text
                style={{
                  fontSize: 24,
                  fontWeight: '700',
                  paddingHorizontal: 20,
                }}>
                Items for sell
              </Text>
              <View
                style={{
                  paddingHorizontal: 20,
                  marginTop: 20,
                  flexDirection: 'row',
                  flexWrap: 'wrap',
                  justifyContent: 'space-between',
                }}>
                {this.state.products.map(p => {
                  return (
                    <Item
                      width={width}
                      name={p.name}
                      type={p.type}
                      price={p.price}
                      rating={p.rating}
                    />
                  );
                })}
                
              </View>
            </View>
          </ScrollView>
        </View>
      </SafeAreaView>
    );
  }
}
export default Explore;
