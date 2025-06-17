/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {

    return new Promise((resolve,reject) => {
        setTimeout(resolve,millis)
    })



    // const promise = new Promise((resolve,reject) => {
    //     setTimeout(() => {
    //         resolve(millis)
    //     },millis)
        
    // })
    
    // return promise.then((res) => res)

  
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */