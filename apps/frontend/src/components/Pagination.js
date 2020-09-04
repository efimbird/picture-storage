import React from "react";
import {render} from "react-dom";


class PaginationPrevious extends React.Component {
  constructor(props) {
    super(props);
    this.onSetPage = this.onSetPage.bind(this)
  }

  onSetPage(e) {
    e.preventDefault();
    this.props.onSetPage(this.props.current - 1)
  }

  render() {
    if (this.props.current > 1) {
      return (
        <li className="pagination-previous">
          <a aria-label="Previous page" onClick={this.onSetPage}>
            Previous <span className="show-for-sr">page</span>
          </a>
        </li>
      );
    }
    return (
      <li className="pagination-previous disabled">
        Previous <span className="show-for-sr">page</span>
      </li>
    );
  }
}


class PaginationNext extends React.Component {
  constructor(props) {
    super(props);
    this.onSetPage = this.onSetPage.bind(this)
  }

  onSetPage(e) {
    e.preventDefault();
    this.props.onSetPage(this.props.current + 1)
  }

  render() {
    if (this.props.current < this.props.total) {
      return (
        <li className="pagination-next">
          <a aria-label="Next page" onClick={this.onSetPage}>
            Next <span className="show-for-sr">page</span>
          </a>
        </li>
      );
    }
    return (
      <li className="pagination-next disabled">
        Next <span className="show-for-sr">page</span>
      </li>
    );
  }
}


class PaginationEllipsis extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    if (!this.props.isNeeded) {
      return ''
    }
    return <li className="ellipsis" aria-hidden="true" />;
  }
}


class PaginationPage extends React.Component {
  constructor(props) {
    super(props);
    this.onSetPage = this.onSetPage.bind(this)
  }

  onSetPage(e) {
    e.preventDefault();
    this.props.onSetPage(this.props.page)
  }

  render() {
    if (this.props.page === this.props.current) {
      return <li className="current"><span className="show-for-sr">You're on page</span> {this.props.page}</li>;
    }
    return <li><a aria-label={'Page ' + this.props.page } onClick={this.onSetPage}>{this.props.page}</a></li>;
  }
}


class Pagination extends React.Component {
  constructor(props) {
    super(props);
    this.paginationNeedsBeginningEllipsis = this.paginationNeedsBeginningEllipsis.bind(this);
    this.paginationNeedsEndingEllipsis = this.paginationNeedsEndingEllipsis.bind(this);
    this.rangeBegin = this.rangeBegin.bind(this);
    this.rangeEnd = this.rangeEnd.bind(this);
    this.paginationRange = this.paginationRange.bind(this);
  }

  paginationNeedsBeginningEllipsis() {
    return this.props.total >= 8 && this.props.page > 4
  }

  paginationNeedsEndingEllipsis() {
    return this.props.total >= 8 && this.props.total - this.props.page > 3
  }

  rangeBegin() {
    if (this.props.total < 8 || this.props.page <= 4) {
      return 2
    }
    if (!this.paginationNeedsEndingEllipsis()) {
      return this.props.total - 4
    }
    return this.props.page - 1
  }

  rangeEnd() {
    if (this.props.total < 8 || this.props.total - this.props.page <= 3) {
      return this.props.total - 1
    }
    if (!this.paginationNeedsBeginningEllipsis()) {
      return 5
    }
    return this.props.page + 1
  }

  paginationRange() {
    if (this.rangeEnd() - this.rangeBegin() + 1 < 0) {
      return []
    }
    return new Array(this.rangeEnd() - this.rangeBegin() + 1).fill().map((d, i) => i + this.rangeBegin());
  }

  render() {
    if (this.props.total <= 1) {
      return ''
    }
    return (
      <nav className="pagination-container" aria-label="Pagination">
        <ul className="pagination">
          <PaginationPrevious current={this.props.page} onSetPage={this.props.onSetPage} />
          <PaginationPage key={1} page={1} current={this.props.page} onSetPage={this.props.onSetPage} />
          <PaginationEllipsis key='ellipsis_begin' isNeeded={this.paginationNeedsBeginningEllipsis()} />
          {this.paginationRange().map((i) => <PaginationPage key={i} page={i} current={this.props.page} onSetPage={this.props.onSetPage} />)}
          <PaginationEllipsis  key='ellipsis_end' isNeeded={this.paginationNeedsEndingEllipsis()} />
          <PaginationPage key={this.props.total} page={this.props.total} current={this.props.page} onSetPage={this.props.onSetPage} />
          <PaginationNext current={this.props.page} total={this.props.total} onSetPage={this.props.onSetPage} />
        </ul>
      </nav>
    );
  }
}

export default Pagination;