import * as dl from '../../src/index';

(async () => {
  const weightsManifestResponse =
      await fetch('./weights/weights_manifest.json');
  const json = await weightsManifestResponse.json();

  const result = await dl.loadWeights(json, './weights', ['weight1']);

  Object.keys(result).forEach(key => {
    const tensor = result[key];
    console.log('-----------' + key + '-----');
    console.log(tensor.shape, tensor.dtype);
    console.log(tensor.dataSync());
  });
})();
