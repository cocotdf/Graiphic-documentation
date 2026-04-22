<h1>Search In Array</h1>

<h2>Description</h2>

<p>Searches for an element in an array starting at start index. The search is linear and the function stops searching as soon as the element is found.</p>

<p align="center"><img src="/_assets/shared-images/af/af9bb0b73772-search_in_array-1.png" alt="Search_In_Array 1.Png" width="220" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Tensor.Png" src="/_assets/shared-images/77/775fe37288a0-input_acc_inference.png" width="42"/></td>
      <td valign="top"><strong>array : <em>class,</em></strong> n-dimentional tensor.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Single.Png" src="/_assets/shared-images/fd/fd47ddc3550b-input_single.png" width="42"/></td>
      <td valign="top"><strong>element : <em>float,</em></strong> value to search for in the array. element must be the same data type as the elements in unsorted array.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_32.Png" src="/_assets/shared-images/05/052f6e6ea35b-input_array_integer_32.png" width="42"/></td>
      <td valign="top"><strong>start index : <em>array,</em></strong> index that function begins the search from.</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Boolean.Png" src="/_assets/shared-images/f4/f4787639135e-output_boolean.png" width="42"/></td>
      <td valign="top"><strong>found ? : <em>boolean,</em></strong> if true, then the element has been found in the array.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_32.Png" src="/_assets/shared-images/fe/fe7405762e7c-output_array_integer_32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>array,</em></strong> index of element is the index where element is found.</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Accelerator library to run it).</p>

<h3>Search In 1D Array</h3>

<p align="center"><img src="assets/ex_search_in_1d_array.png" alt="ex_search_in_1d_array" width="260" /></p>

<h3>Search In 2D Array</h3>

<p align="center"><img src="assets/ex_search_in_2d_array.png" alt="ex_search_in_2d_array" width="260" /></p>

<h3>Search In 3D Array</h3>

<p align="center"><img src="assets/ex_search_in_3d_array.png" alt="ex_search_in_3d_array" width="260" /></p>
