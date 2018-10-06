import React, { Component } from 'react';
import { Text, View, StyleSheet, Image } from 'react-native';

class Charity extends Component {
  constructor(props) {
    super(props);
    this.state = { Charity1: {'organization_name': "GrassRoot Soccer"}, Charity2: {'organization_name': "Marie Curie"}, Charity3: {'organization_name': "Brain and Behavior Research"}, Charity4: {'organization_name': "United Way", Charity5: {'orgnization_name': "Habitats for Humanity"} }
  }
  }

  //organiation_name
  //mission

  render() {
    return (
      <View style={{flex: 1}}> 
        <Text style={{fontSize:24, paddingTop: 30, paddingLeft: 10, paddingBottom: 10 }}>Habitats for Humanity</Text>
        <Image 
        source={require('../Assets/Habitat_for_Humanity.jpg')}
        style={{height: 60, width: null, resizeMode: "contain"}} />
        <Text style={{paddingLeft: 10}}>A world where everyone has a decent place to live </Text>
        <Text style={styles.titleStyles}>GrassRoot Soccer</Text>
         <Image 
        source={require('../Assets/Grassroot.jpg')}
        style={{height: 60, width: null, resizeMode: "contain"}} />
        <Text style={{paddingLeft: 10}}>Grassroot Soccer is an adolescent health organization that leverages the power of soccer to educate, inspire, and mobilize youth </Text>
        <Text style={styles.titleStyles}>United Way</Text>
         <Image 
        source={require('../Assets/UW.jpg')}
        style={{height: 60, width: null, resizeMode: "contain"}} />
        <Text style={{paddingLeft: 10}}>We tackle complex social problems by surrounding North Texas with local solutions in the areas of Education, Income, and Health</Text>
        <Text style={styles.titleStyles}>Marie Curie</Text>
         <Image 
        source={require('../Assets/Marie_Curie.jpg')}
        style={{height: 60, width: null, resizeMode: "contain"}} />
        <Text style={{paddingLeft: 10}}>Our vision is a just world without poverty</Text>
      </View>
    );
  }
}

const styles = {
  titleStyles: {
    padding: 10,
    fontSize: 24
  }
}

export default Charity;

