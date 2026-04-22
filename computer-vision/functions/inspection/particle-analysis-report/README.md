<h1>Particle Analysis Report</h1>

<h2>Description</h2>

<p>Returns the number of particles detected in a binary image and an array of reports containing the most commonly used particle measurements. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/83/83918a8bad68-particle_analysis_report.png" alt="Particle_Analysis_Report.Png" width="336" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class, </em></strong>type accepted <strong>U8</strong>.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Boolean.Png" src="/_assets/shared-images/1c/1cd07c2c1382-input_boolean.png" width="42"/></td>
      <td valign="top"><strong>Connectivity 4/8 (8) :<em> boolean, </em></strong>specifies the type of connectivity used by the algorithm for particle detection. The connectivity mode directly determines whether an adjacent pixel belongs to the same particle or a different particle.
<ul>
<li>
<ul>
<li>True : particle detection is performed in connectivity mode 8</li>
<li>False : particle detection is performed in connectivity mode 4</li>
</ul>
</li>
</ul></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Interger_32.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>Number Of Particles :<em> integer, </em></strong>indicates the number of particles detected in the image.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Ouput_Array_Cluster_2.Png" src="/_assets/shared-images/ce/ce79fc3283cc-cluster-array-out.png" width="42"/></td>
      <td valign="top"><strong>Region Reports : <em>array, </em></strong>returns a set of uncalibrated pixel measurements from the detected particles.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Double.Png" src="/_assets/shared-images/62/628d73130cf9-output_double.png" width="42"/></td>
      <td valign="top"><strong>Area : <em>float, </em></strong>is the area of the particle.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Double.Png" src="/_assets/shared-images/62/628d73130cf9-output_double.png" width="42"/></td>
      <td valign="top">Number of Holes : <em>float, </em>is the number of holes in the particle.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Cluster_1.Png" src="/_assets/shared-images/ed/edf449127715-output_cluster_1.png" width="42"/></td>
      <td valign="top">Bounding Rect : <em>cluster, </em>is the smallest rectangle with sides parallel to the x-axis and y-axis that completely encloses the particle.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Cluster_1.Png" src="/_assets/shared-images/ed/edf449127715-output_cluster_1.png" width="42"/></td>
      <td valign="top"><strong>Center of Mass : <em>cluster, </em></strong>is the point representing the average position of the total mass of the particle assuming every point in the particle has a constant density. <strong>Center of Mass</strong> may be located outside the particle if the particle is not convex.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Double.Png" src="/_assets/shared-images/62/628d73130cf9-output_double.png" width="42"/></td>
      <td valign="top"><strong>Orientation :<em> float, </em></strong>is the angle of the line passing through the particle center of mass with the lowest moment of inertia.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Cluster_1.Png" src="/_assets/shared-images/ed/edf449127715-output_cluster_1.png" width="42"/></td>
      <td valign="top"><strong>Dimensions : <em>cluster, </em></strong>indicates the width and height of <strong>Bounding Rect.</strong></td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img src="assets/region_reports.png" alt="region_reports" width="172" /></p></td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>
