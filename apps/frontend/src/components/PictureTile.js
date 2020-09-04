import React from "react";


class PictureTile extends React.Component {
  get_orientation(picture) {
    if (picture.is_narrow) {
      return '-narrow'
    }
    if (picture.is_wide) {
      return '-wide'
    }
    return ''
  }

  render() {
    let picture = this.props.picture;
    return (
      <div className={'picture-item ' + this.get_orientation(picture)}>
        <a href={'/picture/' + picture.id + '/'} title={picture.title}>
          <img src={picture.image_small_url} alt={picture.title} />
        </a>
      </div>
    );
  }
}

export default PictureTile;