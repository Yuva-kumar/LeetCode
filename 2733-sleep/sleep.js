/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {

    const promise = new Promise((resolve,reject) => {
        setTimeout(() => {
            resolve(millis)
        },millis)
        
    })
    
    return promise.then((res) => res)

  
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */