export const getJson = async (url: string) => {
  try {
    const resp = await fetch(url);
    return await resp.json();
  } catch (e) {
    console.error(`getJson error: ${e}`);
    throw e;
  }
};
