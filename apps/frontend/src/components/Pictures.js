import { render } from 'react-dom';
import React from 'react';
import PictureTile from './PictureTile';
import Pagination from "./Pagination";
import Loader from "./Loader";


class Pictures extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: {
        'results': [],
        'count': 0
      },
      loaded: false,
      placeholder: 'Loading',
      page: props.page,
    };
    this.onSetPage = this.onSetPage.bind(this);
    this.load = this.load.bind(this);
    if (props.title) {
      this.title_query = '&title=' + props.title;
    } else {
      this.title_query = ''
    }
  }

  componentDidMount() {
    this.load(this.state.page);
  }

  load(page) {
    fetch('/api/pictures/?limit=' + this.props.per_page + '&offset=' + ((page - 1) * this.props.per_page) + this.title_query)
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: 'Something went wrong!' };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  onSetPage(pageNumber) {
    this.setState({
      page: pageNumber,
      loaded: false,
    });
    this.load(pageNumber);
  }

  render() {
    return (
      <div>
        <Loader key={this.state.page} />
        <div className='pictures-container'>
          {this.state.data.results.map(picture => {
            return <PictureTile key={picture.id} picture={picture} />;
          })}
        </div>
        <Pagination page={this.state.page} total={Math.ceil(this.state.data.count / this.props.per_page)} onSetPage={this.onSetPage}/>
      </div>
    );
  }
}

export default Pictures;

const container = document.getElementById('main-content');
const params = new URLSearchParams(window.location.search);
const title = params.get('title');
render(<Pictures page={1} per_page={6} title={title} />, container);