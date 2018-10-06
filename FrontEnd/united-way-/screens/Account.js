import React, { Component } from 'react';
import { Text, View, StyleSheet, FlatList, Image } from 'react-native';

import Icon from 'react-native-vector-icons/Ionicons'

class Account extends Component {
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
  render() {
    return (
      <View style={{flex: 1}}>
        <View>
            <View style={styles.header}>
              <View style={styles.headerContent}>
                  <Image style={styles.avatar}/>
                  <Text style={styles.name}>Matt Smith </Text>
              </View>
            </View>

            <View style={styles.body}>
              <Text style={styles.info}>Favorite Charity</Text>
              <Text style={styles.info}>Donations</Text>
            </View>
          </View>

          <View style={{ flex: 1, position: "absolute", bottom: 30, left: 20, right: 20, top: 350, backgroundColor: "white"}}>
              <Text style={{ fontSize: 24, fontWeight: '700',     paddingHorizontal: 20, alignSelf: 'center', paddingTop: 10 }}>
                Leaderboard List
              </Text>
              <Text style={styles.itemStyling}> Robbert Dinero - 47 </Text>
              <Text style={styles.itemStyling}> Margret Thatcher - 48 </Text>
              <Text style={styles.itemStyling}> * Matt Smith * - 49 </Text>
              <Text style={styles.itemStyling}> Bob Marley - 50 </Text>
              <Text style={styles.itemStyling}> Guy Lee - 51 </Text>
          </View>
      </View>
    );
  }
}
export default Account;

const styles = StyleSheet.create({
  header:{
    backgroundColor: "#DCDCDC",
  },
  headerContent:{
    padding:30,
    alignItems: 'center',
  },
  avatar: {
    width: 130,
    height: 130,
    borderRadius: 63,
    borderWidth: 4,
    borderColor: "white",
    marginBottom:10,
  },
  name:{
    fontSize:22,
    color:"#000000",
    fontWeight:'600',
  },
  body:{
    backgroundColor: "#778899",
    height:500,
    alignItems:'center',
  },
  info:{
    fontSize:18,
    marginTop:20,
    color: "#FFFFFF",
  },
  itemStyling: {
    alignSelf: 'center',
    padding: 10
  }
});