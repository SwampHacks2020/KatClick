import React, { Component } from 'react'
import {
    Card, CardImg, CardText, CardBody,
    CardTitle, CardSubtitle, Button
  } from 'reactstrap';

// export class CardView extends Component {
//     constructor(props) {
//         super(props);
//     }

    

//     render() {
//         return (
//             {Example}
//         )
//     }
// }

const CardView = (props) => {
    return (
      <div>
        <Card>
          <CardImg top width="100%" src="../images/nyan.gif" alt="Card image cap" />
          <CardBody>
            <CardTitle>Card title</CardTitle>
            <CardSubtitle>Card subtitle</CardSubtitle>
            <CardText>Some quick example text to build on the card title and make up the bulk of the card's content.</CardText>
            <Button>Button</Button>
          </CardBody>
        </Card>
      </div>
    );
  };



export default CardView
