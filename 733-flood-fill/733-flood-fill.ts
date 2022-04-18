function floodFill(image: number[][], sr: number, sc: number, newColor: number): number[][] {
    const rows = image.length;
    const cols = image[0].length;
    const curColor =  image[sr][sc];
    if (curColor === newColor) return image;
    
    const dfs = (r: number,c: number) => {
      if(image[r][c] == curColor){
        image[r][c] = newColor;
        if(r>=1) dfs(r-1, c);
        if(r+1<rows) dfs(r+1,c);
        if(c>=1) dfs(r, c-1);
        if(c+1<cols) dfs(r,c+1)
      }
    }
    
    dfs(sr, sc);
    return image;
};