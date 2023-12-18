import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { thunkGetAlbum } from "../../redux/album"


const AllAlbum = () => { 
const dispatch = useDispatch()
const [title,setTitle] = useState()

const albums = useSelector(state => Object.values(state.albums))
console.log('this is react album state', albums)

useEffect(() =>  { 
   const fetchFunction = async () => { 
     await dispatch(thunkGetAlbum())
   }
    fetchFunction()
},[dispatch])

return(
  <form action="">
    <label>
        <input type="text"
        value={title}

        
        
        />
    </label>

  </form>



)

}

export default AllAlbum