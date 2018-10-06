import React, { Component } from 'react';
import { Text, View, StyleSheet, TouchableOpacity, ScrollView, Image, Dimensions } from 'react-native';

import Item from './components/Explore/Item'

const { height, width } = Dimensions.get('window');
class Sell extends Component {
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
  loadCamera() {
    return;
  }

  render() {
    return (
      <View style={{ flex:1, justifyContent: "center" }}>
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
                  paddingHorizontal: 100,
                  marginTop: 20,
                  //flexDirection: 'row',
                  //flexWrap: 'wrap',
                  //justifyContent: 'space-between',
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
        <TouchableOpacity
          style={{ "padding": 10, "borderWidth": 1, "backgroundColor": "white", position: "absolute", bottom: 10, left: 25, right: 25, justifyContent: "center", flexDirection: "row"}}
          onPress={this.loadCamera()}
        >
          <Text> Add Item </Text>
        </TouchableOpacity>
      </View>
    );
  }
}
export default Sell;