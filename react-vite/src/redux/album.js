
const GET_ALBUMS = 'getalbums/api/albums'


export const actionAlbum = (album) => { 
    return {
        type:GET_ALBUMS,
        payload: album
    }
}

export const thunkGetAlbum = () => async (dispatch) => { 
    try{  
        const response = await fetch('/api/album/')
        if (response.ok) { 
            const data = await response.json()
            dispatch(actionAlbum(data))
        }
        else { 
            console.log('it is not ok')
            throw new Error('something went wrong with api fetching')
        }
    }

    catch(error) { 
        console.log('this is catch block',error)
        return error
    }

}

const albumReducer = (state={},action) =>{ 
    switch(action.type) { 
      case GET_ALBUMS : { 
        let newState = {}
        let albums = action.payload
        console.log('this is reducer action.payload',albums)
        albums.forEach(album => {
            newState[album.id] = album
        });
        console.log('this is reducer block',newState)
        return newState
      }
      default:
        return state
    }
    
}

export default albumReducer;