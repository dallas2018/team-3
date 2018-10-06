import React, { Component } from "react";
import {
    View,
    Text,
    StyleSheet,
    Image,
    Button
} from "react-native";

import StarRating from 'react-native-star-rating'

class Item extends Component {
  openProduct() {

  }
  render() {
    return (
      <View style={{ width: this.props.width / 2 - 30, height: this.props.width / 2 - 30,                borderWidth: 0.5, borderColor: '#dddddd' }}>
        <View style={{ flex: 1 }}>
          <Image
            style={{ flex: 1, width: null, height: null, resizeMode: 'cover' }}
            source={require('../../../Assets/logitech.jpg')} />
        </View>
        <View style={{ justifyContent: 'center', alignItems: 'center', flexDirection: 'row', flex: 1}}>
        <View style={{ flex: 1, alignItems: 'flex-start', justifyContent: 'space-evenly',                  paddingLeft: 10 }}>
          <Text style={{ fontSize: 10, color: '#b63838' }}>{this.props.type}</Text>
          <Text style={{ fontSize: 12, fontWeight: 'bold' }}>{this.props.name}</Text>
          <Text style={{ fontSize: 10 }}>{this.props.price}$</Text>
          <StarRating
            disable={true}
            maxStars={5}
            rating={this.props.rating}
            starSize={10}
          />
        </View>
        <View>
          <Button
  style={{fontSize: 20, color: 'green'}}
    color="#841584"
    fontSize ={10}
  onPress={() => this._handlePress()}
  title="Buy     "
/>
        </View>
        </View>
        
      </View>
    );
  }
}
export default Item;