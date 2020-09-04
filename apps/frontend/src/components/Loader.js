import React from "react";


class Loader extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loaded: false
    };
  }

  componentDidMount() {
    setTimeout(() => {
      this.setState({
        loaded: true
      });
    }, 1000);
  }

  render() {
    if (this.state.loaded) {
      return '';
    }
    return <div className="loader" />;
  }
}

export default Loader;