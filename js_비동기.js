// JS Promise

// 프로미스의 3가지 상태
// Pending(대기) : 비동기 처리 로직이 아직 완료되지 않은 상태
// Fulfilled(이행) : 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태 (resovle인자로 값을 리턴해줄때)
// Rejected(실패) : 비동기 처리가 실패하거나 오류가 발생한 상태

function getData(callback) {
    // new Promise() 추가
    // 프로미스는 콜백함수로 resolve와 reject인자를 가진다.
    // resolve인자는 비동기 작업 이후 리턴값을 넘겨주는데 사용한다.
    // reject인자는 작업 도중 생긴 오류를 넘겨주는데 사용한다.
    return new Promise(function(resolve, reject) {
      $.get('url 주소/products/1', function(response) {
        // 데이터를 받으면 resolve() 호출
        resolve(response);
      });
    });
  }
  
  // getData()의 실행이 끝나면 호출되는 then()
  getData().then(function(tableData) {
    // then안에 있는 콜백함수 인자로 resolve에 넘겨준 값이 온다.
    // resolve()의 결과 값이 여기로 전달됨
    console.log(tableData); // $.get()의 reponse 값이 tableData에 전달됨
  });


// JS Promise Chaining
new Promise(function(resolve, reject){
    setTimeout(function() {
      resolve(1);
    }, 2000);
  })
  .then(function(result) {
    console.log(result); // 1
    return result + 10;
  })
  .then(function(result) {
    console.log(result); // 11
    return result + 20;
  })
  .then(function(result) {
    console.log(result); // 31
  });
// then 메서드를 이용하여 리턴값을 계속 넘겨줄수있다.
// then구문에서 넘겨주는값이 프로미스객체이면 체이닝을 통해 다시 받아서 처리해 주어야한다.


// JS Promise ALL
const userList = [
    { name: 'ethan', id: 1 },
    { name: "david", id: 2 },
    { name: 'john', id: 3 }
  ];
  
  // 1초가 걸리는 쿼리
  const getUserById = async (id) => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        const [user] = userList.filter(user => user.id === id)
        resolve(user)
      }, 1000)
    })
  }
  
  // 2초가 걸리는 쿼리
  const getAllUsers = () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve(userList)
      }, 2000)
    })
  }
  
  const fetchData = async () => {
    console.time('소요시간 : ')
    // await로 비동기를 관리하게 되면 하나의 await가 끝나기 전까지 다른 작업을 할수없게된다.
    // 만일 두개의 await작업이 서로 관계가 없는 작업이라면 효율적이지 못한것이다.
    // 이럴때 promise all를 사용하면 좋다.
    const user = await getUserById(2)
    const userList = await getAllUsers()
    
    // 서로 관계가 없는 비동기 작업을 하려면 프로미스 올을 사용하여 두 작업을 동시에 처리하게 한다.
    // const [user, userList] = await Promise.all([getUserById(2), getAllUsers()])
    console.log(user)
    console.log(userList)
    console.timeEnd('소요시간 : ')
  }
  
  fetchData()