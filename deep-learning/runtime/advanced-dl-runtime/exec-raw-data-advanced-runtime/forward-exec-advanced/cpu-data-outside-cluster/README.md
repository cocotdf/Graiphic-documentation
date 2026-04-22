<h1>Inputs CPU Raw Data (data outside cluster)</h1>

<h2>Description</h2>

<p>Run the model with the raw input data from the CPU, the output buffer is allocated automatically. The raw data are passed outside the cluster, since very large clusters may reduce performance.</p>

<p align="center"><img alt="CPU (Data outside cluster)" src="assets/CPU (Data outside cluster).png" width="220"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Inference.Png" src="/_assets/shared-images/9d/9d8d8a8daf63-input_inference.png" width="42"/></td>
      <td valign="top"><strong>Inference in</strong> <strong>: <em>object, </em></strong>inference session.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="32"/><strong>Inputs Info : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_64.Png" src="/_assets/shared-images/71/712313814f21-input_array_integer_64.png" width="42"/></td>
      <td valign="top"><strong>inputs_shapes :<em> array, </em></strong>specifies the shape of the input tensor. Since the data is stored as a flattened 1D buffer, this shape is necessary to reconstruct the original dimensions.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_64.Png" src="/_assets/shared-images/71/712313814f21-input_array_integer_64.png" width="42"/></td>
      <td valign="top">inputs string length : <em>array, </em>used when the tensor type is string. If the tensor has shape <code>[5,3]</code>, this field contains 15 values, each representing the length of a corresponding string element. This ensures that the actual size of <code>inputs_data</code> is known despite variable string lengths.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_64.Png" src="/_assets/shared-images/71/712313814f21-input_array_integer_64.png" width="42"/></td>
      <td valign="top">inputs_ranks :<em> array, </em>indicates the rank of the tensor, i.e. the number of dimensions (Scalar = 0, 1D = 1, 2D = 2, etc.).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Enum.Png" src="/_assets/shared-images/05/05126b56ff83-input_array_enum.png" width="42"/></td>
      <td valign="top">inputs_types :<em> array, </em>defines the ONNX tensor type as an enumerated value (e.g. FLOAT, INT64, STRING).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Unsigned_8.Png" src="/_assets/shared-images/f7/f7e8b09da0a0-input_array_unsigned_8.png" width="42"/></td>
      <td valign="top"><strong>inputs_data : <em>array, </em></strong>contains the raw byte representation of the input tensor data, stored as a 1D flattened buffer.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="input_param_inference_forward_cpu_2" src="/_assets/shared-images/4f/4ff07b637a4b-input_param_inference_forward_cpu.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Inference.Png" src="/_assets/shared-images/fc/fc9dc35d411a-output_inference.png" width="42"/></td>
      <td valign="top"><strong>Inference out</strong> <strong>: <em>object, </em></strong>inference session.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Cluster Out.Png" src="/_assets/shared-images/0a/0a479d27b394-cluster-out.png" width="32"/><strong>Outputs Info : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_64.Png" src="/_assets/shared-images/8a/8a3ecb76444e-output_array_integer_64.png" width="42"/></td>
      <td valign="top"><strong>output_shapes_array :<em> array, </em></strong>specifies the shape of the input tensor. Since the data is stored as a flattened 1D buffer, this shape is necessary to reconstruct the original dimensions.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_64.Png" src="/_assets/shared-images/8a/8a3ecb76444e-output_array_integer_64.png" width="42"/></td>
      <td valign="top">output_strings_length_array : <em>array, </em>used when the tensor type is string. If the tensor has shape <code>[5,3]</code>, this field contains 15 values, each representing the length of a corresponding string element. This ensures that the actual size of <code>inputs_data</code> is known despite variable string lengths.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_64.Png" src="/_assets/shared-images/8a/8a3ecb76444e-output_array_integer_64.png" width="42"/></td>
      <td valign="top">output_ranks_array :<em> array, </em>indicates the rank of the tensor, i.e. the number of dimensions (Scalar = 0, 1D = 1, 2D = 2, etc.).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Out Array Integer 32.Png" src="/_assets/shared-images/fe/fe7405762e7c-output_array_integer_32.png" width="42"/></td>
      <td valign="top">output_types_array :<em> array, </em>defines the ONNX tensor type as an enumerated value (e.g. FLOAT, INT64, STRING).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Unsigned_8.Png" src="/_assets/shared-images/ee/eeb63aea4468-output_array_unsigned_8.png" width="42"/></td>
      <td valign="top"><strong>outputs_raw_data : <em>array, </em></strong>contains the raw byte representation of the input tensor data, stored as a 1D flattened buffer.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="output_param_inference_forward_cpu_2" src="/_assets/shared-images/00/00a78083d8f6-output_param_inference_forward_cpu.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
